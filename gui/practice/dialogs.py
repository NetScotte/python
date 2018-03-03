# include QInputDialog , QColorDialog , QFontDialog

# QInputDialog
'''
import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QPushButton,QInputDialog,QLineEdit)


# include QInputDialog , QColorDialog , QFontDialog
#click dialog button and input your name ,then it will be shown in mainwindow
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # the size of button and lineEdit is equal by default
        self.btn1 = QPushButton('dialog', self)
        self.btn1.move(30,20)
        self.btn1.clicked.connect(self.showdialog)

        self.le = QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('dialog')
        self.show()

    def showdialog(self):
        # 弹出可编辑对话框，标题input dialog, 标签enter your name
        text, ok = QInputDialog.getText(self, 'input Dialog','Enter your name:')
        if ok:
            self.le.setText(str(text))
'''

# QColorDialog
'''
import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QFrame,QPushButton,QColorDialog)
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0,0,0)

        self.dialog = QPushButton('dialog',self)
        self.dialog.move(50,30)
        self.dialog.clicked.connect(self.showDialog)

        # 如果设置的位置值过大，会覆盖前面的按钮
        self.fr = QFrame(self)
        self.fr.setStyleSheet('QWidget { background-color: %s }'
            % col.name())
        self.fr.setGeometry(130,22,100,100)

        self.setGeometry(300,300,250,180)
        self.setWindowTitle('color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid:
            self.fr.setStyleSheet("QWidget { background-color: %s}"%col.name())
'''

# QFontDialog

import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,QVBoxLayout,QLabel,QFontDialog,QSizePolicy,QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        # 对于部件，这里需要self,为了在其他方法中使用，所以标签用了self命名
        btn = QPushButton('dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        btn.move(20,20)

        self.lb = QLabel('Knowledge only matters:',self)
        self.lb.move(130,20)

        btn.clicked.connect(self.showDialog)
        vbox.addWidget(btn)
        vbox.addWidget(self.lb)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.lb.setFont(font)


# QFileDialog
'''
import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QTextEdit,QAction,QFileDialog)
from PyQt5.QtGui import QIcon

# QMainWindow is more powerfull than Qwidget
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        openFile = QAction(QIcon('web.png'),'&open',self)
        openFile.setShortcut('ctrl+o')
        openFile.setStatusTip('open file')
        openFile.triggered.connect(self.showDialog)

        self.statusBar()

        menuBar = self.menuBar()
        file = menuBar.addMenu('&File')
        file.addAction(openFile)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'open file','/home')
        if fname[0]:
            try:
                # 如果打开失败，转一次ansi即可，也不是都行的通
                f = open(fname[0],'r')
                with f:
                    text = f.read()
                    self.textEdit.setText(text)
            except:
                self.textEdit.setText('fail opened')
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())       # it will terminate as soon as you run without this