# QPixmap, a QLineEdit, a QSplitter, and a QComboBox.

'''
# QPixmap
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    # 这里图片大小不可调节,
    def initUI(self):

        # hbox = QHBoxLayout(self)      # 如果不设置布局管理器，那么会占据整个窗口，也是不可调节
        pixmap = QPixmap("web.png")     # 图片对象，image widget

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
'''

# QlineEdit
# 这里只粘贴两个方法：lineEdit.textChanged[str].connect(self.onChanged), self.label.adjustSize()

# QSpliter
'''
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
    QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
# 为窗口设置layout,layout中添加splitter,splitter中再添加其他可调部件
        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        #  use a styled frame in order to see the boundaries between the QFrame widgets
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
'''

# QcomboBox
'''
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")
        combo.move(50, 50)
        combo.activated[str].connect(self.onActivated)

        def onActivated(self, text):
            self.lbl.setText(text)
            self.lbl.adjustSize()
'''