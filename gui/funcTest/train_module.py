# 此模块用于放置与训练相关的信息,包括设置参数等
# 可用于观察训练过程和结果，由plt负责展示，此处调用Plt并弹窗

from PyQt5.QtWidgets import QWidget,QLabel,QVBoxLayout

class Training(QWidget):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        label = QLabel('training')
        vbox.addWidget(label)
        self.setLayout(vbox)
        self.setWindowTitle('training')

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ex = Training()
    ex.show()
    sys.exit(app.exec_())