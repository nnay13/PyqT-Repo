import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Signals & Slots"
        top = 200
        left = 500
        width = 300
        height = 250
        iconName = "icon.jpg"
        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
