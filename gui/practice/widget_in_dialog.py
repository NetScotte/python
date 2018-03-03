import sys
from PyQt5.QtWidgets import (QMainWindow,QTabWidget,QLabel, QApplication,QVBoxLayout,QPushButton,QWidget,QDialog)


# 如果将dialog改为QMainWindow就无法呈现
class Example(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # menu = self.menuBar()
        # file = menu.addMenu('file')

        tabWidget = QTabWidget()
        tabWidget.addTab(firstTab(), "General")
        tabWidget.addTab(secondTab(), "Permissions")
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)

class firstTab(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label= QLabel('first')
        print('1')
        self.setCentralWidget(self.label)

class secondTab(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel('second')
        print('2')
        self.setCentralWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

