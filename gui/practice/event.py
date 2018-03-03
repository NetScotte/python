
'''
# 只有if __name__....是公用的，使用此部分需要uncomment，
# basic event handler
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QApplication,QLCDNumber,QSlider,QVBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # it seems transparent if there is no self or Qt.Horizontal
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        sld.valueChanged.connect(lcd.display)

        self.setLayout(vbox)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('lcd and slider')
        self.show()

    # reimplement event handler
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:         # Qt.key_Escape的兄弟负责处理各种按键
            self.close()
'''

'''
# determine the signal source
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('ok',self)
        btn1.move(30,50)
        btn2 = QPushButton('cancel',self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClick)      # 有那些signal,为什么不能加()
        btn2.clicked.connect(self.buttonClick)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('event handler')
        self.show()

    # 该方法名任意
    def buttonClick(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text()+' was pressed')  # self.statusBar是已有对象，可以直接显示消息
'''

# custom signal
# I want to know how many signals there are
import sys
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QMainWindow,QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('custom signal')
        self.show()

    # reimplement function, you can reimplement others
    def mousePressEvent(self, event):
        self.c.closeApp.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())