import sys
from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    # 这里图片大小不可调节,
    def initUI(self):

        # hbox = QHBoxLayout(self)      # 如果不设置布局管理器，那么会占据整个窗口，也是不可调节
        pixmap = QPixmap("../practice/web.png")     # 图片对象，image widget

        lb = QLabel(self)
        lb.setPixmap(pixmap)
        lb.setFixedSize(300,300)
        self.setCentralWidget(lb)
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())