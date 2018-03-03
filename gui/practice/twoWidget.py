from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QVBoxLayout,QAction
from PyQt5.QtGui import QIcon

# 同时显示两个窗口
class firstTab(QMainWindow):
    def __init__(self):
        super().__init__()
        showAction = QAction(QIcon('../practice/web.png'),'show',self)
        showAction.triggered.connect(self.showWidget)

        showTool = self.addToolBar('show')
        showTool.addAction(showAction)

    def showWidget(self):
        self.second = secondTab()
        self.second.show()

class secondTab(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel('second')
        self.setCentralWidget(label)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = firstTab()
    ex.show()
    sys.exit(app.exec_())