import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QColor,QFont,QBrush
from PyQt5.QtCore import Qt


# drag text 将那一串编码转为了字体
'''
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('painting')
        self.show()

    def paintEvent(self, e):
        paint = QPainter()
        paint.begin(self)           # 丢失self出现秒退
        self.drawText(e,paint)
        paint.end()

    def drawText(self,event,paint):
        paint.setPen(QColor(168,34,3))
        paint.setFont(QFont('Arial',10))
        paint.drawText(event.rect(),Qt.AlignCenter,self.text)
'''

import sys,random
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QPen,QColor
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('paint point')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawText(e,qp)
        qp.end()

    def drawText(self,e,qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1,size.width()-1)
            y = random.randint(1,size.height()-1)
            qp.drawPoint(x,y)

    #color
    # def drawRectangles(self, qp):
    #     col = QColor(0, 0, 0)
    #     col.setNamedColor('#d4d4d4')
    #     qp.setPen(col)
    #
    #     qp.setBrush(QColor(200, 0, 0))  # draw the background of a shape
    #     qp.drawRect(10, 15, 90, 60)
    #
    #     qp.setBrush(QColor(255, 80, 0, 160))
    #     qp.drawRect(130, 15, 90, 60)
    #
    #     qp.setBrush(QColor(25, 0, 90, 200))
    #     qp.drawRect(250, 15, 90, 60)

    # QPen
    # def drawLines(self, qp):
    #     pen = QPen(Qt.black, 2, Qt.SolidLine)     # colour is black. The width is set to 2 pixels, pen style
    #
    #     qp.setPen(pen)
    #     qp.drawLine(20, 40, 250, 40)
    #
    #     pen.setStyle(Qt.DashLine)     # 产生各种值，如直线，虚线，点线等
    #     qp.setPen(pen)
    #     qp.drawLine(20, 80, 250, 80)  # x1,y1,x2,y2
    #
    #     pen.setStyle(Qt.DashDotLine)
    #     qp.setPen(pen)
    #     qp.drawLine(20, 120, 250, 120)
    #
    #     pen.setStyle(Qt.DotLine)
    #     qp.setPen(pen)
    #     qp.drawLine(20, 160, 250, 160)
    #
    #     pen.setStyle(Qt.DashDotDotLine)
    #     qp.setPen(pen)
    #     qp.drawLine(20, 200, 250, 200)
    #
    #
    #     pen.setStyle(Qt.CustomDashLine)       # custom pen styles
    #     pen.setDashPattern([1, 4, 5, 4])      # pattern is 1px dash, 4px space, 5px dash, 4px space
    #     qp.setPen(pen)
    #     qp.drawLine(20, 240, 250, 240)

        # Qbrush    three different types: a predefined brush, a gradient, or a texture pattern.
    # def drawBrushes(self, qp):
    #     brush = QBrush(Qt.SolidPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(10, 15, 90, 60)       # 起始位置x,y,width,height
    #
    #     brush.setStyle(Qt.Dense1Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(130, 15, 90, 60)
    #
    #     brush.setStyle(Qt.Dense2Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(250, 15, 90, 60)
    #
    #     brush.setStyle(Qt.DiagCrossPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(10, 105, 90, 60)
    #
    #     brush.setStyle(Qt.Dense5Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(130, 105, 90, 60)
    #
    #     brush.setStyle(Qt.Dense6Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(250, 105, 90, 60)
    #
    #     brush.setStyle(Qt.HorPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(10, 195, 90, 60)
    #
    #     brush.setStyle(Qt.VerPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(130, 195, 90, 60)
    #
    #     brush.setStyle(Qt.BDiagPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(250, 195, 90, 60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
