'''
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QToolTip,QPushButton,QMessageBox)
from PyQt5.QtGui import QFont

# 测试案例，用来感受熟悉pyqt的各种方法
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        QToolTip.setFont(QFont('SansSerif',10))

        self.setToolTip('this is a <b>Qwidget</b> widget')      # 这在主窗体中显示
        btn = QPushButton('button',self)
        btn.setToolTip('this is a <b>QPushButton</b> widget')   # 当鼠标放在按钮上时显示
        # btn.clicked.connect(QCoreApplication.instance().quit) # 点击按钮退出程序
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,220)
        self.setWindowTitle('toolTip')
        # self.setWindowIcon(QIcon('web.png'))        # 以当前目录为基准，没有图片不会报错

        self.show()

    # 退出行为
    def closeEvent(self, event):
        # parameters:parent, title, info, button, default
        reply = QMessageBox.question(self,'Message','Are you sure to quit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__=='__main__':
    app = QApplication(sys.argv)

    ex = Example()
    # w.resize(250,150)     # 默认比这大多了
    # w.move(300,300)       # 默认位于窗口中间

    sys.exit(app.exec_())
'''

# center window
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250,150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    # 默认也是位于中间
    def center(self):
        qr = self.frameGeometry()           # 获得一个矩形指示主窗口的形状,即PyQt5.QtCore.QRect(0, 0, 249, 149)
        cp = QDesktopWidget().availableGeometry().center()
        # 获得显示器的分辨率PyQt5.QtCore.QRect(0, 0, 1366, 728)，然后获得中间位置PyQt5.QtCore.QPoint(682, 363)
        qr.moveCenter(cp)           # 将矩形移到中间

        self.move(qr.topLeft())     # 将应用程序移动到矩形的中间

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())