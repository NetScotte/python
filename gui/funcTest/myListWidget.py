from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import Qt

class myListWidget(QListWidget):
    def __init__(self,s):
        super().__init__(s)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.list = ['leave','drop','leave','drop']

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        self.list.append('drop')

    def dragLeaveEvent(self, e):
        self.list.remove('leave')