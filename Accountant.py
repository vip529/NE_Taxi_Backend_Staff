from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = QDesktopWidget().screenGeometry().width()
        self.h = QDesktopWidget().screenGeometry().height()-68
        self.initWindow()

        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("Accountant Main Page")
        self.showMaximized()
        self.setFixedSize(self.w, self.h)
        print(str(self.w)+"\n"+str(self.h))
        self.show()
    def initWindow(self):
        self.setStyleSheet("font-size: 17px")
        self.logout = QToolButton(self)
        self.logout.move(self.w*.95, 30)
        self.logout.setFixedSize(25, 25)
        self.logout.setIcon(QIcon("logout.png"))
        self.logout.setIconSize(QSize(25, 25))
        self.logout.setStyleSheet("border: 0px transparent;")
        self.logout.setMask(QRegion(self.logout.rect(), QRegion.Ellipse))
        self.logout.setToolTip("Logout")
        self.logout.clicked.connect(self.logOut)
        self.year = QComboBox(self)
        self.year.addItems(["Select Year","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028"])
        self.year.move(100, 50)
        self.year.resize(120,30)
        self.month = QComboBox(self)
        self.month.move(245,50)
        self.month.resize(120,30)
        self.month.addItems(["Select Month", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
        self.date = QComboBox(self)
        self.date.addItem("Select Date")
        self.date.move(390,50)
        self.date.resize(120,30)
        self.turnOver = QLabel("",self)
        self.showTurnOver()
        self.turnOver.move(200,130)
        self.creditLabel = QLabel("",self)
        self.showCredit()
        self.creditLabel.move(self.w*.7,130)
        self.creditButton = QPushButton("Credit",self)
        self.creditButton.move(self.w*.8165,self.h*.3)
        self.debitButton = QPushButton("Debit", self)
        self.debitButton.move(self.w*.8715, self.h*.3)
        self.b2cButton = QPushButton("B 2 C Packages", self)
        self.b2cButton.move(80, self.h*.3)
        self.b2cListBox = QListWidget(self)
        self.b2cListBox.setGeometry(80,245,self.w*.864, self.h*.585)
        self.b2cListBox.setSpacing(7)
        self.b2cListBox.setStyleSheet("font-size: 20px;")
        self.b2cButton.clicked.connect(self.b2cList)
        self.widget = QWidget(self)
        self.styleWidget(self.widget)
        self.widgetDriver = QWidget(self)
        self.styleWidget(self.widgetDriver)
        self.wdgtDrvrList = QWidget(self)
        self.styleWidget(self.wdgtDrvrList)
        self.wdgtAgntList = QWidget(self)
        self.styleWidget(self.wdgtAgntList)
        self.widgetAgent = QWidget(self)
        self.styleWidget(self.widgetAgent)
        self.wdgtEmployeeList = QWidget(self)
        self.styleWidget(self.wdgtEmployeeList)
        self.widgetEmployee = QWidget(self)
        self.styleWidget(self.widgetEmployee)
        self.widgetCredit = QWidget(self)
        self.styleWidget(self.widgetCredit)
        self.widgetCnfrm = QWidget(self)
        self.styleWidget(self.widgetCnfrm)
        self.widgetMMT = QWidget(self)
        self.styleWidget(self.widgetMMT)
        self.widgetNEWeb = QWidget(self)
        self.styleWidget(self.widgetNEWeb)
        self.widgetOther = QWidget(self)
        self.styleWidget(self.widgetOther)
        self.debitFor = QComboBox(self.widget)
        self.debitFor.addItems(["Select","Driver","Permit Agent","Employee"])
        self.debitFor.adjustSize()
        self.debitFor.setGeometry(100, 70, 450, 30)
        self.drvrList = QListWidget(self.wdgtDrvrList)
        self.locateList(self.drvrList)
        self.drvrList.move(1, 58)
        self.drvrList.resize(1177, 340)
        self.agentList = QListWidget(self.wdgtAgntList)
        self.locateList(self.agentList)
        self.employeeList = QListWidget(self.wdgtEmployeeList)
        self.locateList(self.employeeList)
        self.creditFor = QComboBox(self.widgetCredit)
        self.creditFor.addItems(["Select", "Make My Trip", "NE Website", "Others"])
        self.creditFor.setGeometry(100,70,450,30)
        self.mmtList = QListWidget(self.widgetMMT)
        self.locateList(self.mmtList)
        self.neList = QListWidget(self.widgetNEWeb)
        self.locateList(self.neList)
        self.otherList = QListWidget(self.widgetOther)
        self.locateList(self.otherList)
        self.b2cList()
        self.debitFor.currentTextChanged.connect(self.debitOption)
        self.creditFor.currentTextChanged.connect(self.creditOption)
        self.debitButton.clicked.connect(self.debit)
        self.creditButton.clicked.connect(self.credit)
        self.date.currentTextChanged.connect(self.b2cConnect)
        self.year.currentTextChanged.connect(self.datesSet)
        self.month.currentTextChanged.connect(self.datesSet)
        self.drvrList.itemDoubleClicked.connect(self.driver)
        self.agentList.itemDoubleClicked.connect(self.agent)
        self.employeeList.itemDoubleClicked.connect(self.employee)
        self.b2cListBox.itemDoubleClicked.connect(self.b2cPkgDtail)
        self.mmtList.itemDoubleClicked.connect(self.b2bPkgDtail)
        self.neList.itemDoubleClicked.connect(self.b2bPkgDtail)
        self.otherList.itemDoubleClicked.connect(self.b2bPkgDtail)
        self.copyright = QLabel("© NE Taxi 2019. All Rights Reserved.", self)
        self.copyright.setStyleSheet('''color: white; background-color: black; font-weight: bold; text-align: left;''')
        self.copyright.setAlignment(Qt.AlignCenter)
        self.statusBar = self.statusBar()
        self.statusBar.addPermanentWidget(self.copyright, 50)
    def logOut(self):
        self.close()
    def showTurnOver(self):
        self.turnOver.clear()
        sum=0
        if self.year.currentText() != "Select Year" and self.month.currentText() != "Select Month" and self.date.currentText() != "Select Date":
            with self.conn:
                cur = self.conn.cursor()
                dateTime = self.year.currentText() + "-" + self.month.currentText() + "-" + self.date.currentText()
                cur.execute("SELECT * FROM nepackages WHERE Date = %s",[dateTime,])
                row = cur.fetchall()
                if row:
                    for col in row:
                        sum=sum+float(col[12])
        turnOver="Total TurnOver : "+str(sum)
        self.turnOver.setText(turnOver)
        self.turnOver.adjustSize()
    def showCredit(self):
        self.creditLabel.clear()
        sum=0
        if self.year.currentText() != "Select Year" and self.month.currentText() != "Select Month" and self.date.currentText() != "Select Date":
            with self.conn:
                cur = self.conn.cursor()
                dateTime = self.year.currentText() + "-" + self.month.currentText() + "-" + self.date.currentText()
                cur.execute("SELECT * FROM nepackages WHERE Date = %s",[dateTime,])
                row = cur.fetchall()
                if row:
                    for col in row:
                        if col[13]!=None:
                            sum=sum+float(col[13])
        creditLabel = "Total Credit Amount : "+str(sum)
        self.creditLabel.setText(creditLabel)
        self.creditLabel.adjustSize()
    def b2cConnect(self):
        pass
    def datesSet(self):
        self.date.clear()
        if self.year.currentText() != "Select Year" and self.month.currentText() != "Select Month":
            if self.month.currentText() in ["01", "03", "05", "07", "08", "10", "12"]:
                for d in range(1, 32):
                    self.date.addItem(str(d))
            elif self.month.currentText() in ["04", "06", "07", "11"]:
                for d in range(1, 31):
                    self.date.addItem(str(d))
            elif self.month.currentText() == "02":
                self.yr = int(self.year.currentText())
                if self.yr % 4 == 0 and (self.yr % 100 != 0 or self.yr % 400 == 0):
                    for d in range(1, 30):
                        self.date.addItem(str(d))
                else:
                    for d in range(1, 29):
                        self.date.addItem(str(d))
            self.b2cConnect()
        else:
            self.date.addItem("Select Date")
    def styleWidget(self,widget):
        widget.setGeometry(82, 245, self.w*.864, self.h*.585)
        frame = QLabel(widget)
        frame.resize(self.w*.864, self.h*.585)
        frame.setStyleSheet("background-color: white; inset grey; min-height: 200px;")
        frame.setFrameShape(QFrame.Panel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setLineWidth(3)
    def locateList(self,list):
        list.setStyleSheet("font-size: 20px;")
        list.setSpacing(5)
        list.move(1, 58)
        list.resize(self.w*.861, self.h/2)
    def b2cList(self):
        self.widgetMMT.hide()
        self.widgetOther.hide()
        self.widgetNEWeb.hide()
        self.widget.hide()
        self.wdgtDrvrList.hide()
        self.widgetDriver.hide()
        self.wdgtAgntList.hide()
        self.widgetAgent.hide()
        self.wdgtEmployeeList.hide()
        self.widgetEmployee.hide()
        self.widgetCredit.hide()
        self.widgetCnfrm.hide()
        self.b2cListBox.clear()

    def b2cPkgDtail(self,item):
        if self.year.currentText() != "Select Year" and self.month.currentText() != "Select Month" and item.text() != "No Package to Show":
            self.b2cListBox.hide()
            self.backbtn = QToolButton(self.widgetCnfrm)
            self.showBackBtn()
            self.backbtn.clicked.connect(self.b2cList)
            self.pkgDetail(item)
    def b2bPkgDtail(self,item):
        if self.year.currentText() != "Select Year" and self.month.currentText() != "Select Month" and item.text() != "No Package to Show":
            self.widgetMMT.hide()
            self.widgetNEWeb.hide()
            self.widgetOther.hide()
            self.backbtn = QToolButton(self.widgetCnfrm)
            self.showBackBtn()
            self.backbtn.clicked.connect(self.credit)
            self.pkgDetail(item)
    def pkgDetail(self,item):
        pass
    def creditCnfrm(self):
        pass
    def debitOption(self):
        self.widget.hide()
        if self.debitFor.currentText() == "Driver":
            self.driverList()
        if self.debitFor.currentText() == "Permit Agent":
            self.agntList()
        if self.debitFor.currentText() == "Employee":
            self.employeList()
    def driverList(self):
        self.backbtn = QToolButton(self.wdgtDrvrList)
        self.showBackBtn()
        self.backbtn.clicked.connect(self.debit)
        self.drvrListLbl = QLabel("Driver List", self.wdgtDrvrList)
        self.drvrListLbl.move(400, 8)
        self.drvrListLbl.setStyleSheet("font-size: 25px;")
        self.drvrListLbl.adjustSize()
        self.drvrList.clear()

    def driver(self):
        self.wdgtDrvrList.hide()
        self.backbtn = QToolButton(self.widgetDriver)
        self.showBackBtn()
        self.backbtn.clicked.connect(self.debit)
        self.driverLabel = QLabel("Driver Name : ",self.widgetDriver)
        self.driverLabel.move(90,42)
        self.driverName = QLineEdit(self.widgetDriver)
        self.driverName.setPlaceholderText("Driver Name")
        self.driverName.move(200,40)
        regex = QRegExp("[a-zA-Z ]+")
        self.strValidator = QRegExpValidator(regex)
        self.driverName.setValidator(self.strValidator)
        self.fromDestLabel = QLabel("FROM : ",self.widgetDriver)
        self.fromDestLabel.move(680,42)
        self.fromDest = QLineEdit(self.widgetDriver)
        self.fromDest.move(750,40)
        self.fromDest.setPlaceholderText("FROM")
        self.toDestLabel = QLabel("TO : ",self.widgetDriver)
        self.toDestLabel.move(880,42)
        self.toDest = QLineEdit(self.widgetDriver)
        self.toDest.move(920,40)
        self.toDest.setPlaceholderText("To")
        self.dDTransNoLbl = QLabel("Transaction No. : ", self.widgetDriver)
        self.dDTransNoLbl.move(280, 82)
        self.dDTransNo = QLineEdit(self.widgetDriver)
        self.dDTransNo.move(420, 80)
        self.dDTransNo.setPlaceholderText("To")
        self.dDAmntLabl = QLabel("Debit Amount : ",self.widgetDriver)
        self.dDAmntLabl.move(400,82)
        self.dDAmnt = QLineEdit(self.widgetDriver)
        self.intValidator = QDoubleValidator(0.00,0.00,2)
        self.dDAmnt.move(520, 80)
        self.dDAmnt.setPlaceholderText("Debit Amount")
        self.dDAmnt.setValidator(self.intValidator)
        self.dbtFrDrvr = QPushButton("Debit",self.widgetDriver)
        self.dbtFrDrvr.move(450,120)
        self.dbtFrDrvr.setStyleSheet("font-size: 20px;")
        self.dbtFrDrvr.clicked.connect(self.dbtToDrvr)
        self.widgetDriver.show()
    def dbtToDrvr(self):
        pass
    def agntList(self):
        self.backbtn = QToolButton(self.wdgtAgntList)
        self.showBackBtn()
        self.backbtn.clicked.connect(self.debit)
        self.agntListLbl = QLabel("Agent List", self.wdgtAgntList)
        self.agntListLbl.move(400, 8)
        self.agntListLbl.setStyleSheet("font-size: 25px;")
        self.agntListLbl.adjustSize()
        self.agentList.clear()

    def agent(self):
        self.wdgtAgntList.hide()
        self.backbtn = QToolButton(self.widgetAgent)
        self.showBackBtn()
        self.backbtn.clicked.connect(self.debit)
        self.agentNameLabel = QLabel("Agent Name : ",self.widgetAgent)
        self.agentNameLabel.move(100,42)
        self.agentName = QLineEdit(self.widgetAgent)
        self.agentName.move(200, 40)
        self.agentName.setPlaceholderText("Agent Name")
        regex = QRegExp("[a-zA-Z ]+")
        self.strValidator = QRegExpValidator(regex)
        self.agentName.setValidator(self.strValidator)
        self.refPrmtLabel = QLabel("Ref No. : ", self.widgetAgent)
        self.refPrmtLabel.move(400, 42)
        self.refPrmtNo = QLineEdit(self.widgetAgent)
        self.refPrmtNo.move(500, 40)
        self.refPrmtNo.setPlaceholderText("Ref No.")
        self.destLabel = QLabel("Destination : ", self.widgetAgent)
        self.destLabel.move(880, 42)
        self.dest = QLineEdit(self.widgetAgent)
        self.dest.move(920, 40)
        self.dest.setPlaceholderText("Destination Name")
        self.dPAmntLabl = QLabel("Debit Amount : ", self.widgetAgent)
        self.dPAmntLabl.move(400, 82)
        self.dPAmnt = QLineEdit(self.widgetAgent)
        self.intValidator = QIntValidator()
        self.dPAmnt.move(520, 100)
        self.dPAmnt.setPlaceholderText("Debit Amount")
        self.dPAmnt.setValidator(self.intValidator)
        self.dbtFrPrmt = QPushButton("Debit", self.widgetAgent)
        self.dbtFrPrmt.move(450, 120)
        self.dbtFrPrmt.setStyleSheet("font-size: 20px;")
        self.dbtFrPrmt.clicked.connect(self.dbtToAgent)
        self.widgetAgent.show()
    def dbtToAgent(self):
        pass
    def employeList(self):
        self.backbtn = QToolButton(self.wdgtEmployeeList)
        self.showBackBtn()
        self.backbtn.clicked.connect(self.debit)
        self.employeeListLbl = QLabel("Employee List", self.wdgtEmployeeList)
        self.employeeListLbl.move(400, 8)
        self.employeeListLbl.setStyleSheet("font-size: 25px;")
        self.employeeListLbl.adjustSize()
        self.employeeList.clear()

    def employee(self):
        self.wdgtEmployeeList.hide()
        self.backbtn = QToolButton(self.widgetEmployee)
        self.showBackBtn()
        self.backbtn.clicked.connect(self.debit)
        self.employeeNameLabel = QLabel("Employee Name : ",self.widgetEmployee)
        self.employeeNameLabel.move(100, 42)
        self.employeeName = QLineEdit(self.widgetEmployee)
        self.employeeName.move(250, 40)
        self.employeeName.setPlaceholderText("Employee Name")
        regex = QRegExp("[a-zA-Z ]+")
        self.strValidator = QRegExpValidator(regex)
        self.employeeName.setValidator(self.strValidator)
        self.employeeIdLabel = QLabel("Employee ID : ", self.widgetEmployee)
        self.employeeIdLabel.move(500, 42)
        self.employeeId = QLineEdit(self.widgetEmployee)
        self.employeeId.move(650, 40)
        self.employeeId.setPlaceholderText("Employee ID")
        self.employeeSalaryLabl = QLabel("Debit Amount : ", self.widgetEmployee)
        self.employeeSalaryLabl.move(400, 82)
        self.employeeSalary = QLineEdit(self.widgetEmployee)
        self.intValidator = QIntValidator()
        self.employeeSalary.move(550, 80)
        self.employeeSalary.setPlaceholderText("Debit Amount")
        self.employeeSalary.setValidator(self.intValidator)
        self.dbtFrSalary = QPushButton("Debit", self.widgetEmployee)
        self.dbtFrSalary.move(450, 120)
        self.dbtFrSalary.setStyleSheet("font-size: 20px;")
        self.dbtFrSalary.clicked.connect(self.dbtToEmployee)
        self.widgetEmployee.show()
    def dbtToEmployee(self):
        pass
    def debit(self):
        self.b2cListBox.hide()
        self.widgetMMT.hide()
        self.widgetOther.hide()
        self.widgetNEWeb.hide()
        self.wdgtDrvrList.hide()
        self.widgetDriver.hide()
        self.wdgtAgntList.hide()
        self.widgetAgent.hide()
        self.wdgtEmployeeList.hide()
        self.widgetEmployee.hide()
        self.widgetCredit.hide()
        self.widgetCnfrm.hide()
        self.b2cButton.setStyleSheet('''font-size: 20px; background-color: red; color: white; padding: 5px 10px;''')
        self.creditButton.setStyleSheet('''font-size: 20px; font-weight: normal; background-color: green;color: white; padding: 5px 10px;''')
        self.debitButton.setStyleSheet('''font-size: 20px; font-weight: normal; background-color: blue; color: white; padding: 5px 10px;''')
        self.debitFor.setCurrentText("Select")
        self.widget.show()
    def showBackBtn(self):
        self.backbtn.setIcon(QIcon("Back.ico"))
        self.backbtn.setFixedSize(30, 30)
        self.backbtn.setIconSize(QSize(30, 30))
        self.backbtn.move(20, 18)
        self.backbtn.setStyleSheet("border: 0px transparent;")
        self.backbtn.setMask(QRegion(self.backbtn.rect(), QRegion.Ellipse))
        self.backbtn.setToolTip("Back")
    def credit(self):
        self.b2cListBox.hide()
        self.widgetMMT.hide()
        self.widgetOther.hide()
        self.widgetNEWeb.hide()
        self.widget.hide()
        self.wdgtDrvrList.hide()
        self.widgetDriver.hide()
        self.wdgtAgntList.hide()
        self.widgetAgent.hide()
        self.wdgtEmployeeList.hide()
        self.widgetEmployee.hide()
        self.widgetCnfrm.hide()
        self.creditFor.setCurrentText("Select")
        self.b2cButton.setStyleSheet('''font-size: 20px; background-color: red; color: white; padding: 5px 10px;''')
        self.creditButton.setStyleSheet('''font-size: 20px; font-weight: normal; background-color: blue; color: white; padding: 5px 10px;''')
        self.debitButton.setStyleSheet('''font-size: 20px; font-weight: normal; background-color: red; color: white; padding: 5px 10px;''')
        self.widgetCredit.show()
    def creditOption(self):
        pass
    def mmt(self):
        pass

    def neWeb(self):
        pass
    def others(self):
        pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())