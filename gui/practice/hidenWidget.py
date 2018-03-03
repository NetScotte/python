from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QPushButton, QStackedWidget,
                             QVBoxLayout, QWidget)


# 此部分实现了对部件进行添加和移除，对部件进行显隐
class PyMultiPageWidget(QWidget):

    def __init__(self, parent=None):
        super(PyMultiPageWidget, self).__init__(parent)
        self.value=0

        self.bt = QPushButton('switch',self)
        self.bt.clicked.connect(self.switch)

        self.stackWidget = QStackedWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.bt)
        self.layout.addWidget(self.stackWidget)
        self.setLayout(self.layout)
        self.resize(500,400)

    def switch(self):
        self.value = 1 - self.value
        bt = QPushButton('new')
        if self.value:
            self.addPage(bt)
        else:
            self.removePage(0)

    @pyqtSlot(QWidget)
    def addPage(self, page):
        index = self.stackWidget.count()
        page.setParent(self.stackWidget)
        self.stackWidget.insertWidget(index, page)

    @pyqtSlot(int)
    def removePage(self, index):
        widget = self.stackWidget.widget(index)
        self.stackWidget.removeWidget(widget)



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = PyMultiPageWidget()
    widget.show()
    sys.exit(app.exec_())
