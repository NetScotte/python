from PyQt5.QtWidgets import (QWidget,QPushButton,QLabel,QLineEdit,QTextEdit,QGroupBox,QGridLayout,QRadioButton,
                             QVBoxLayout,QHBoxLayout)
from PyQt5.QtWidgets import QApplication


# 需要的设置有：
# 黑白名单，可以添加名单，显示列表
# 设置算法
# 更正识别结果
# 为什么相同的代码，别的可以运行，我的就运行不了,此种情况多是示例为Qwidget,而我的是Qmainwindow
class Setting(QWidget):
    def __init__(self):
        super(Setting,self).__init__()

        type = self.wordList('白名单')
        hint = self.wordList('黑名单')

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(type)
        mainLayout.addWidget(hint)
        self.setLayout(mainLayout)

        self.setWindowTitle("setting")

    def wordList(self,name):
        typeGroupBox = QGroupBox(name)

        # 窗口部件
        wordEdit = QLineEdit()
        wordButton = QPushButton('add')
        wordText = QTextEdit()

        # 布局
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(wordEdit)
        hbox.addWidget(wordButton)
        vbox.addLayout(hbox)
        vbox.addWidget(wordText)
        typeGroupBox.setLayout(vbox)

        return typeGroupBox


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    ex = Setting()
    ex.show()
    sys.exit(app.exec_())