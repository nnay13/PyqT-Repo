import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Qt5 Main Window"
        self.top = 100
        self.left = 100
        self.height = 600
        self.width = 800
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
