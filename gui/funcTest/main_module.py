# 此为主模块
# 用于检测使用，选择一封邮件，并显示系统处理结果，可以通过菜单栏文件选择一封邮件
# 可展示当前文件内容,此处应该使用dockfile，三个dockwidget,分别表示显示内容，正常邮件，垃圾邮件，如果之后有需求
# 可以增加分类
# 可以移动正常邮件和垃圾邮件里的文件
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor,QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QDockWidget,QListWidget, QMainWindow,
                             QFileDialog,QTextEdit)

from myListWidget import myListWidget

from setting_module import Setting
from train_module import Training

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createAction()
        self.createToolBar()
        self.createDockWindows()

        self.setWindowTitle("main window")

    # 显示toolbar，并指向执行函数
    def createAction(self):
        self.openAction = QAction('open',self)
        self.openAction.setShortcut('ctrl+o')
        self.openAction.triggered.connect(self.openfile)

        self.settingAction = QAction('setting',self)
        self.settingAction.setShortcut('ctrl+alt+s')
        self.settingAction.triggered.connect(self.setting)

        self.trainAction = QAction('training',self)
        self.trainAction.setShortcut('ctrl+t')
        self.trainAction.triggered.connect(self.training)

    # 显示工具栏
    def createToolBar(self):

        openfile = self.addToolBar('open')
        setting = self.addToolBar('setting')
        training = self.addToolBar('train')

        openfile.addAction(self.openAction)
        setting.addAction(self.settingAction)
        training.addAction(self.trainAction)

    #打开文件的对话框
    def openfile(self):
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

    # 显示setting窗口,出现闪退,添加self后没有此问题
    def setting(self):
        self.setWidget = Setting()
        self.setWidget.show()

    # 显示training窗口
    def training(self):
        self.trainWidget = Training()
        self.trainWidget.show()

    def showDockContent(self, paragraph):
        self.showtext(paragraph)

    # 找到一个方法，当点击某项后，显示此项内容，首先获取此项,可以控制列表，对列表增删
    # 想象是展示主题，点击主题后显示对应内容，然后可以通过拖放进行增删
    def createDockWindows(self):
        dock = QDockWidget("正常邮件", self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.customerList = myListWidget(dock)
        self.customerList.addItems((
            "John Doe, Harmony Enterprises, 12 Lakeside, Ambleton",
            "Jane Doe, Memorabilia, 23 Watersedge, Beaton",
            "Tammy Shea, Tiblanka, 38 Sea Views, Carlton",
            "Tim Sheen, Caraba Gifts, 48 Ocean Way, Deal",
            "Sol Harvey, Chicos Coffee, 53 New Springs, Eccleston",
            "Sally Hobart, Tiroli Tea, 67 Long River, Fedula"))
        dock.setWidget(self.customerList)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        dock = QDockWidget("垃圾邮件", self)
        self.paragraphsList = myListWidget(dock)
        self.paragraphsList.addItems((
            "Thank you for your payment which we have received today.",
            "Your order has been dispatched and should be with you within "
                "28 days.",
            "We have dispatched those items that were in stock. The rest of "
                "your order will be dispatched once all the remaining items "
                "have arrived at our warehouse. No additional shipping "
                "charges will be made.",
            "You made a small overpayment (less than $5) which we will keep "
                "on account for you, or return at your request.",
            "You made a small underpayment (less than $1), but we have sent "
                "your order anyway. We'll add this underpayment to your next "
                "bill.",
            "Unfortunately you did not send enough money. Please remit an "
                "additional $. Your order will be dispatched as soon as the "
                "complete amount has been received.",
            "You made an overpayment (more than $5). Do you wish to buy more "
                "items, or should we return the excess to you?"))
        dock.setWidget(self.paragraphsList)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        self.customerList.currentTextChanged.connect(self.showDockContent)
        self.paragraphsList.currentTextChanged.connect(self.showDockContent)

    # 在编辑框里显示内容
    def showtext(self,content=''):
        self.textEdit.clear()
        self.textEdit.setText(content)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

