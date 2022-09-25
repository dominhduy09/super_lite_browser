
# Duyhandsome's Browser - Super Lite Browser (SLB)
from multiprocessing import set_forkserver_preload
import sys
from PyQt5.QtCore import * # line 11
from PyQt5.QtWidgets import * # line 7 --> most important
from PyQt5.QtWebEngineWidgets import * # line 10


# window main
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com")) # set URL
        self.setCentralWidget(self.browser) # show in center
        self.showMaximized() # auto show in maximized or nothing will happen
# Super Lite Browser (SLB) was created! --> with no function 


# navbar
        navbar = QToolBar()
        self.addToolBar(navbar)


        home_button = QAction("Home", self) # home_button and name
        home_button.triggered.connect(self.navigate_home) # connect to main window and action
        navbar.addAction(home_button) # add to navbar

        back_button = QAction("Back", self) # back_button and name
        back_button.triggered.connect(self.browser.back) # connect to main window and action
        navbar.addAction(back_button) # add to navbar

        reload_button = QAction("Reload", self) # reload_button and name
        reload_button.triggered.connect(self.browser.reload) # connect to main window and action
        navbar.addAction(reload_button) # add to navbar

        forward_button = QAction("Forward", self) # forward_button and name
        forward_button.triggered.connect(self.browser.forward) # connect to main window and action
        navbar.addAction(forward_button) # add to navbar


        self.url_bar = QLineEdit() # url_bar created
        self.url_bar.returnPressed.connect(self.navigate_to_url) # connect to main window and action
        navbar.addWidget(self.url_bar) # add to navbar

        self.browser.urlChanged.connect(self.update_url) 


    def navigate_home (self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url (self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url (self, q):
        self.url_bar.setText(q.toString())
           
        
# window app
app = QApplication(sys.argv)
QApplication.setApplicationName("Super Lite Browser (SLB)")
window = MainWindow()
app.exec_()