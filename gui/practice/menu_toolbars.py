import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction, qApp,QTextEdit)
from PyQt5.QtGui import QIcon

# MainWindows下的menuBar,toolBar,statusBar,添加方法不是add,就是直接为名字，
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    # statusBar
    # def initUI(self):
    #     self.statusBar().showMessage('Ready')
    #
    #     self.setGeometry(300,300,250,150)
    #     self.setWindowTitle('statusBar')
    #     self.show()


    # menuBar
    # def initUI(self):
    #     exitAction = QAction(QIcon('web.png'),'&Exit',self) # 图标，名称，快捷键
    #     exitAction.setShortcut('Ctrl+Q')    # 快捷键，可以有效使用
    #     exitAction.setStatusTip('Exit application')
    #
    #     exitAction.triggered.connect(qApp.quit)     # 退出行为
    #
    #     self.statusBar()
    #
    #     menuBar = self.menuBar()
    #     fileMenu = menuBar.addMenu('&File')         # 加&的区别是什么
    #     fileMenu.addAction(exitAction)
    #
    #     self.setGeometry(300,300,300,200)
    #     self.setWindowTitle('Menu')
    #     self.show()

    # toolBar
    # def  initUI(self):
    #     exitAction = QAction(QIcon('web.png'),'&Exit',self)     # &没有造成影响，快捷键大小写也没有造成影响
    #     exitAction.setShortcut('ctrl+q')
    #     exitAction.triggered.connect(qApp.quit)
    #
    #     self.toolBar = self.addToolBar('&Exit')
    #     self.toolBar.addAction(exitAction)
    #
    #     self.setGeometry(300,300,300,200)
    #     self.setWindowTitle('ToolBar')
    #     self.show()

    # all
    def initUI(self):
        text = QTextEdit()
        self.setCentralWidget(text)

        # 此处不仅是行动，而且也是菜单下的一个功能，菜单下的功能叫QAction?
        exitAction = QAction(QIcon('web.png'),'Exit',self)
        exitAction.setShortcut('ctrl+q')
        exitAction.setStatusTip('exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menu = self.menuBar()
        file = menu.addMenu('file')
        file.addAction(exitAction)

        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(exitAction)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Bar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())