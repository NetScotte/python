# drag and drop
# it is difficult to understand
# 写出一个方法，用于将文件拖动到编辑框，显示其内容

# drag lineEdit text to button for changing button text
'''
import sys
from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        self.setText(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)           # 被拖动方需要激活
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
'''

# drag button for relayout
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import Qt, QMimeData      # Qt里面存放了很多按键（键盘和鼠标）
from PyQt5.QtGui import QDrag


class myButton(QPushButton):
    def __init__(self,text,parent):
        super().__init__(text,parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return

        #  QDrag object is created. The class provides support for MIME-based drag and drop data transfer.
        # drag and drop two things: data or some graphical objects
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        # start() method of the drag object starts the drag & drop operation
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self,e):
        QPushButton.mousePressEvent(self,e)         # 如果修改为super()，一旦单击就退出了
        if e.buttons() == Qt.LeftButton:
            print('press')

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 接收方需要激活此方法
        self.setAcceptDrops(True)
        self.btn = myButton('Button',self)
        self.btn.move(100,65)

        self.setWindowTitle('click or move')
        self.setGeometry(300,300,300,200)
        self.show()

    # 同上，接收方需要实现dragEnterEvent,dropEvent两个方法
    # 用于判断是否接受
    def dragEnterEvent(self, e):
        e.accept()

    # 用于定义放下时的行为
    def dropEvent(self,e):
        position = e.pos()
        self.btn.move(position)

        # specify the type of the drop action
        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex=Example()
    # ex.show()     # 此处的变化不会产生影响
    # app.exec_()
    sys.exit(app.exec_())