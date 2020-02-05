import Login
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *


class Operation(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.layout()

    #def layout(self):

        self.title = self.setWindowTitle("Operation Department")
        self.setGeometry(160, 70, 1600, 910)
        self.setWindowIcon(QtGui.QIcon("Info.jpg"))

        self.toolbar = QToolBar()
        self.toolbar.setStyleSheet("width:180px; height: 70px")
        self.toolbar.setMovable(False)

        self.driver = QtWidgets.QToolButton()
        self.driver.setText("Driver Details")
        self.driver.setStyleSheet("margin-left: 5px; margin-right: 2px;background-color: #cbcbb3;font-size: 18px;")
        self.driver.setToolTip("<p>For Driver Details</p>")
        self.driver.clicked.connect(self.driver_detail)

        self.Guest = QtWidgets.QToolButton()
        self.Guest.setText("Guest Details")
        self.Guest.setStyleSheet("margin-right: 2px;background-color: #cbcbb3; font-size: 18px;")
        self.Guest.setToolTip("<p>for Guest Details</p>")
        self.Guest.clicked.connect(self.guest_detail)

        self.logout = QtWidgets.QLabel(self)
        self.logout.setPixmap(QtGui.QPixmap("logout.png"))
        self.logout.mouseReleaseEvent = self.Logout



        self.toolbar.addWidget(self.driver)
        self.toolbar.addWidget(self.Guest)
        self.toolbar.addWidget(self.logout)
        self.addToolBar(self.toolbar)


        self.copyright = QLabel("© NE Taxi 2019. All Rights Reserved.",self)
        self.copyright.setStyleSheet(" color: black;  background-color: white; font-size: 15px;   ")
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.addPermanentWidget(self.copyright,50)

    def driver_detail(self):

        self.main = QWidget(self)
        self.setCentralWidget(self.main)
        self.date = QtWidgets.QDateEdit()
        self.date.setFixedWidth(200)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnWidth(500,1)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setAlternatingRowColors(True)
        item = QTableWidgetItem()
        item.setText("Driver")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
       # item = self.tableWidget.horizontalHeaderItem(0)
        #item.setText(_translate("Form", "drivers"))



        self.save = QPushButton("Save")
        self.save.setFixedWidth(200)
        vbox = QVBoxLayout()
        vbox.addWidget(self.date)
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.save)
        self.main.setLayout(vbox)


    def child(self,event):
        v = "ulsydvcs"
        self.lebel.setText(v)

    def guest_detail(self):
        self.main = QWidget(self)
        self.setCentralWidget(self.main)
        self.date = QtWidgets.QDateEdit()
        self.date.setFixedWidth(200)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        self.save = QPushButton("Save")
        vbox = QVBoxLayout()
        vbox.addWidget(self.date)
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.save)
        self.main.setLayout(vbox)

    def account(self):
        pass

    def acc(self):
        pass

    def Logout(self,event):

        self.ui = Login.Login()
        self.ui.show()
        self.close()




    def clicked(self):
         print("clicked")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    oper = Operation()
    oper.show()
    sys.exit(app.exec_())
