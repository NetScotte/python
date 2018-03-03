import sys
#from PyQt5.QtWidgets import QApplication,QHBoxLayout,QVBoxLayout,QWidget,QPushButton
#from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QGridLayout)
from PyQt5.QtWidgets import (QWidget,QApplication,QGridLayout,QLineEdit,QTextEdit,QLabel)


# 布局形式，绝对坐标，QHBoxLayout与QVBoxLayout，gridLayout
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # QHBoxLayout,QVBoxLayout
    # def initUI(self):
    #     # 添加两个按钮
    #     okButton = QPushButton('ok')
    #     cancelButton = QPushButton('cancel')
    #
    #     #使用水平方框布局，添加了可伸展空间和两个按钮
    #     hbox = QHBoxLayout()
    #     hbox.addStretch(1)
    #     hbox.addWidget(okButton)
    #     hbox.addWidget(cancelButton)
    #
    #     vbox = QVBoxLayout()
    #     vbox.addStretch(1)
    #     vbox.addLayout(hbox)
    #
    #     self.setLayout(vbox)
    #
    #     self.setGeometry(300,300,300,200)
    #     self.setWindowTitle('layout')
    #     self.show()

    # gridLayout, a calculator
    # def initUI(self):
    #     grid = QGridLayout()
    #     self.setLayout(grid)
    #
    #     names = ['cls','Bck','','Close',
    #              '7','8','9','/',
    #              '4','5','6','*',
    #              '1','2','3','-',
    #              '0','.','=','+']
    #
    #     positions = [(i,j) for i in range(5) for j in range(4)]
    #
    #     for position,name in zip(positions,names):
    #         if name=='':
    #             continue
    #         button = QPushButton(name)
    #         grid.addWidget(button,*position)
    #
    #     self.setGeometry(300,300,300,200)
    #     self.setWindowTitle('calculator')
    #     self.show()

    # a form which shows grid span multi rows and colums
    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)     # spacing between grid
        self.setLayout(grid)    # position it ends in example,there is no difference

        # label
        titleLabel = QLabel('title')
        authorLabel = QLabel('author')
        reviewLabel = QLabel('review')

        # edit
        titleEdit = QLineEdit('title')
        authorEdit = QLineEdit('name')
        reviewEdit = QTextEdit()

        # add to grid which can be start with 0
        grid.addWidget(titleLabel,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(authorLabel,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(reviewLabel,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        # normal end
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('form')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())