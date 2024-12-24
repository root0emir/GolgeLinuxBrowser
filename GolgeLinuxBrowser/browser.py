import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Ana yapı
        self.browser_tabs = QTabWidget()
        self.setCentralWidget(self.browser_tabs)

        # Başlangıç sekmesi
        self.new_tab()

        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Geri', self)
        back_btn.triggered.connect(self.go_back)
        navbar.addAction(back_btn)

        forward_btn = QAction('İleri', self)
        forward_btn.triggered.connect(self.go_forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Yenile', self)
        reload_btn.triggered.connect(self.reload_page)
        navbar.addAction(reload_btn)

        home_btn = QAction('Ana Sayfa', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        new_tab_btn = QAction('Yeni Sekme', self)
        new_tab_btn.triggered.connect(self.new_tab)
        navbar.addAction(new_tab_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser_tabs.currentChanged.connect(self.update_url_bar)

    def new_tab(self):
        # Yeni sekme açma
        tab = QWebEngineView()
        self.browser_tabs.addTab(tab, "Yeni Sekme")
        tab.setUrl(QUrl("https://duckduckgo.com/"))
        tab.urlChanged.connect(self.update_url)
        self.browser_tabs.setCurrentWidget(tab)

        
        close_button = QPushButton('×')  # X işareti için Unicode karakteri kullanılıyor.
        close_button.clicked.connect(self.close_tab)

   
        close_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #FF6347;  /* Kırmızı renk */
                font-size: 18px;
                font-weight: bold;
                padding: 0;
                margin: 0;
                width: 20px;
                height: 20px;
                border-radius: 50%;
            }
            QPushButton:hover {
                background-color: rgba(255, 99, 71, 0.2);  /* Hover efekti: kırmızımsı ton */
                color: #FF6347;
            }
        """)

        
        tab_index = self.browser_tabs.indexOf(tab)
        self.browser_tabs.tabBar().setTabButton(tab_index, QTabBar.RightSide, close_button)

    def close_tab(self):
        # Aktif sekmeyi kapat
        current_tab_index = self.browser_tabs.currentIndex()
        self.browser_tabs.removeTab(current_tab_index)

    def navigate_home(self):
        # Ana sayfaya git
        current_tab = self.browser_tabs.currentWidget()
        if current_tab:
            current_tab.setUrl(QUrl("https://duckduckgo.com/"))

    def navigate_to_url(self):
        # URL'ye git
        url = self.url_bar.text()
        current_tab = self.browser_tabs.currentWidget()
        if current_tab:
            current_tab.setUrl(QUrl(url))

    def update_url(self, q):
        # URL çubuğunu güncelle
        self.url_bar.setText(q.toString())

    def update_url_bar(self):
        # Aktif sekme değiştiğinde URL'yi güncelle
        current_tab = self.browser_tabs.currentWidget()
        if current_tab:
            self.url_bar.setText(current_tab.url().toString())

    def go_back(self):
        # Geri git
        current_tab = self.browser_tabs.currentWidget()
        if current_tab:
            current_tab.back()

    def go_forward(self):
        # İleri git
        current_tab = self.browser_tabs.currentWidget()
        if current_tab:
            current_tab.forward()

    def reload_page(self):
        # Sayfayı yenile
        current_tab = self.browser_tabs.currentWidget()
        if current_tab:
            current_tab.reload()


app = QApplication(sys.argv)
QApplication.setApplicationName('Golge Browser')
window = MainWindow()
window.show()
app.exec_()
