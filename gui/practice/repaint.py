import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QAction)
from PyQt5.QtGui import QPainter,QFont,QColor,QIcon
from PyQt5.QtCore import Qt


# 此处采用painter工具控制自定义图形的显隐
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.exitLe=0
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('../practice/web.png'), 'change', self)
        exitAction.triggered.connect(self.setLe)

        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(exitAction)

        self.resize(500,400)
        self.setWindowTitle('Red Rock')
        self.show()

    def setLe(self):
        self.exitLe = 1 - self.exitLe
        self.update()
        print('click,exitLe is:%s'%self.exitLe)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QColor(168, 34, 3))
        painter.setFont(QFont('Arial', 10))
        if self.exitLe:
            painter.drawText(event.rect(), Qt.AlignCenter, 'hello')
        else:
            painter.drawText(event.rect(), Qt.AlignCenter, '')
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())