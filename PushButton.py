import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtGui
from PyQt5 import QtCore


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
        self.UIComponents()
        self.show()

    def UIComponents(self):
        button = QPushButton("Cliquez moi", self)
        button.setGeometry(200, 200, 200, 100)
        button.setIcon(QtGui.QIcon("icon.jpg"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip("Il faut cliquer")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
