# QCheckBox, a ToggleButton, a QSlider, a QProgressBar, and a QCalendarWidget.

# core cod
# QCheckBox
'''

    cb = QCheckBox('Show title', self)
    cb.move(20, 20)
    cb.toggle()         # check the checkbox
    cb.stateChanged.connect(self.changeTitle)

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
'''


# toggle button
'''
self.col = QColor(0, 0, 0)
redb = QPushButton('Red', self)
redb.setCheckable(True)
redb.move(10, 10)

redb.clicked[bool].connect(self.setColor)

self.square = QFrame(self)
self.square.setGeometry(150, 20, 100, 100)
self.square.setStyleSheet("QWidget { background-color: %s }" %
self.col.name())

def setColor(self, pressed):
    source = self.sender()

    if pressed:
        val = 255
    else: val = 0

    if source.text() == "Red":
        self.col.setRed(val)
    elif source.text() == "Green":
        self.col.setGreen(val)
    else:
        self.col.setBlue(val)

    self.square.setStyleSheet("QFrame { background-color: %s }" %
        self.col.name())
'''



# slider button
'''
from PyQt5.QtGui import QPixmap
sld = QSlider(Qt.Horizontal, self)
sld.setFocusPolicy(Qt.NoFocus)
sld.setGeometry(30, 40, 100, 30)
sld.valueChanged[int].connect(self.changeValue)

self.label = QLabel(self)
self.label.setPixmap(QPixmap('mute.png'))
self.label.setGeometry(160, 40, 80, 30)

def changeValue(self, value):
    if value == 0:
    self.label.setPixmap(QPixmap('mute.png'))
'''



# progressBar
'''
import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar,
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()                      # 有两个方法，start,stop
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    # Each QObject and its descendants have a timerEvent() event handle
    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)           # 设置进度条的进度


    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')           # 设置按钮的显示内容
        else:
            self.timer.start(100, self)         # 100ms,每间隔100ms，执行一次timerEvent,显然是reimplement
            self.btn.setText('Stop')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
'''



# QCalendarWidget
'''
import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
    QLabel, QApplication)
from PyQt5.QtCore import QDate

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        def showDate(self, date):
            self.lbl.setText(date.toString())
'''

