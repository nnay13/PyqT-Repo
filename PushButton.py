import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Qt5 Push Button"
        top = 200
        left = 500
        width = 800
        height = 600
        iconName = "icon.jpg"
        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
