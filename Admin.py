import mysql.connector
import Login
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
db = mysql.connector.connect(user='root', password='Vipin@123',
                              host='127.0.0.1',
                              database='NETaxi')
mydb = db.cursor()



class Admin(QMainWindow):

    def __init__(self):
        super(Admin, self).__init__()

        self.title = self.setWindowTitle("Administrator Portal")
        self.setGeometry(160, 70, 1600, 910)
        self.setWindowIcon(QtGui.QIcon("Info.jpg"))

        self.toolbar = QToolBar()
        self.toolbar.setStyleSheet("width:180px; height: 70px")
        self.toolbar.setMovable(False)

        self.Package_status = QtWidgets.QToolButton()
        self.Package_status.setText("Package Status")
        self.Package_status.setStyleSheet("margin-left: 5px; margin-right: 2px;background-color: #cbcbb3;font-size: 18px;")
        self.Package_status.setToolTip("<p>For Package Status</p>")
        self.Package_status.clicked.connect(self.package)

        self.Create_Info = QtWidgets.QToolButton()
        self.Create_Info.setText("Create Package Info")
        self.Create_Info.setStyleSheet("margin-left: 5px; margin-right: 2px;background-color: #cbcbb3;font-size: 18px;")
        self.Create_Info.setToolTip("<p>For Package Status</p>")
        self.Create_Info.clicked.connect(self.package_info)

        self.Employee = QtWidgets.QToolButton()
        self.Employee.setText("Employee")
        self.Employee.setStyleSheet("margin-right: 2px;background-color: #cbcbb3; font-size: 18px;")
        self.Employee.setToolTip("<p>for Employee Details</p>")
        self.Employee.clicked.connect(self.employee)

        self.Logout = QtWidgets.QLabel(self)
        self.Logout.setPixmap(QtGui.QPixmap("logout.png"))
        self.Logout.mouseReleaseEvent = self.logout


        self.toolbar.addWidget(self.Create_Info)
        self.toolbar.addWidget(self.Employee)
        self.toolbar.addWidget(self.Package_status)
        self.toolbar.addWidget(self.Logout)
        self.addToolBar(self.toolbar)


        self.copyright = QLabel("© NE Taxi 2019. All Rights Reserved.",self)
        self.copyright.setStyleSheet(" color: black;  background-color: white; font-size: 15px;   ")
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.addPermanentWidget(self.copyright,50)

    def package_info(self):
        self.main = QWidget(self)
        self.setCentralWidget(self.main)
        self.center = QFrame()
        self.center.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form = QFormLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.center)
        self.place = QComboBox()
        self.place.addItems(["Select","Sikkim and Darjeeling","Rest of NE","Bhutan"])
        self.place.setFixedWidth(400)
        self.place.setFixedHeight(26)
        self.submit = QPushButton("Submit")
        self.submit.setFixedWidth(200)
        hbox = QHBoxLayout()
        hbox.addWidget(self.place)
        hbox.addWidget(self.submit)
        self.form.addRow("Region",hbox)
        self.center.setLayout(self.form)
        self.main.setLayout(vbox)
        self.submit.clicked.connect(self.region)
        self.sikkim = QComboBox()
        self.sikkim.setFixedWidth(400)
        self.submit1 = QPushButton("Submit")
        self.submit1.setFixedWidth(200)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.sikkim)
        hbox1.addWidget(self.submit1)
        self.form.addRow("Places", hbox1)
        self.submit1.clicked.connect(self.places)








    def region(self):

        if (self.place.currentText() == "Sikkim and Darjeeling"):
             self.sikkim.addItems(["Gangtok","Lachen","Lachung"])

        if (self.place.currentText() == "Rest of NE"):
            self.sikkim.addItems(["Guwahati", "Kaziranga", "Shillong"])

        if (self.place.currentText() == "Bhutan"):
            self.sikkim.addItems(["Timphu", "Kaziranga", "Shillong"])


    def places(self):

        self.sightseen = QLineEdit()
        self.outstation = QLineEdit()
        self.cost = QLineEdit()
        self.btn = QPushButton("Create or Update")
        self.btn.setFixedWidth(200)
        self.form.addRow("Sightseen",self.sightseen)
        self.form.addRow("Outstation",self.outstation)
        self.form.addRow("Cost", self.cost)
        self.form.addRow("",self.btn)
        self.btn.clicked.connect(self.insert)


    def insert(self):
        region = self.place.currentText()
        place = self.sikkim.currentText()
        sightseen = self.sightseen.text()
        outstation = self.outstation.text()
        cost = self.cost.text()
        value = (region, place, sightseen, outstation, cost)
        data = "INSERT INTO Place VALUES(%s,%s,%s,%s,%s)"
        try:
            mydb.execute(data, value)
            db.commit()
            self.mbox = QMessageBox.information(self, 'Alert', 'Successfully Updated')
        except:
            self.mbox = QMessageBox.information(self, 'Alert', 'Sorry Try  again')







    def employee(self):

        self.main = QWidget(self)
        self.setCentralWidget(self.main)
        self.scrollarea = QScrollArea()
        self.scrollarea.setWidgetResizable(True)
        self.topleft = QFrame()
        self.topleft.setFixedWidth(400)
        self.topleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topright = QFrame()
        self.topright.setFrameShape(QtWidgets.QFrame.StyledPanel)


        self.p1 = QPushButton("Employees")
        self.p2 = QPushButton("Add New Employee")
        hbox = QHBoxLayout()
        hbox.addWidget(self.topleft)
        hbox.addWidget(self.scrollarea)

        vbox = QVBoxLayout()
        vbox.addWidget(self.p1)
        vbox.addWidget(self.p2)
        vbox.addStretch()
        self.topleft.setLayout(vbox)
        self.main.setLayout(hbox)
        self.p2.clicked.connect(self.new_employee)
        self.p1.clicked.connect(self.employees)

    def employees(self):
        for i in range(len(self.topright.children())):
            self.topright.children()[i].deleteLater()


        vbox = QVBoxLayout()

        mydb.execute("SELECT * FROM Employees")
        for row in mydb:
            self.frame = QFrame()
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFixedHeight(300)
            self.lebel = QLabel(row[1])
            hbox = QHBoxLayout()
            hbox.addWidget(self.lebel)
            self.frame.setLayout(hbox)
            vbox.addWidget(self.frame)

        self.topright.setLayout(vbox)
        self.scrollarea.setWidget(self.topright)


    def new_employee(self):

        for i in range(len(self.topright.children())):
            self.topright.children()[i].deleteLater()
        vbox = QVBoxLayout()
        self.form = QFormLayout()

        lebel = QLabel("Details For New Employee:")
        lebel.setStyleSheet("font-size:25px;")
        self.dept = QComboBox()
        self.dept.addItems(["Select","Sales", "Accounts", "Admin","Operation"])

        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("First Name")

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Last Name")

        self.dob = QDateEdit()
        self.dob.setCalendarPopup(True)

        self.gender = QComboBox()
        self.gender.addItems(['Gender','Male','Female','Others'])

        hbox = QHBoxLayout()
        hbox.addWidget(self.first_name)
        hbox.addWidget(self.last_name)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.dob)
        hbox1.addWidget(self.gender)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter Username")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter Password")

        self.photo = QPushButton("browse")
        self.path = QLineEdit()
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.photo)
        hbox3.addWidget(self.path)
        self.photo.clicked.connect(self.getfiles)

        save = QPushButton("Save")
        save.setFixedWidth(200)
        save.setFixedHeight(40)
        save.setStyleSheet("font-size:20px")
        save.clicked.connect(self.employee_details)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(save)

        self.form.addRow(lebel)
        self.form.addRow("Department", self.dept)
        self.form.addRow("Name",hbox)
        self.form.addRow("DOB & Gender",hbox1)
        self.form.addRow("Username",self.username)
        self.form.addRow("Password",self.password)
        self.form.addRow("Upload",hbox3)
        self.form.addRow(hbox2)
        self.form.setSpacing(30)
        self.topright.setLayout(self.form)
        self.scrollarea.setWidget(self.topright)


    def getfiles(self):
        self.fileName = QFileDialog.getOpenFileName(self, 'Single File', 'C:\'', '*.jpg')
        #self.ui.lineEdit.setText(fileName)
        self.path.setText(self.fileName[0])

    def package(self):
        self.main = QWidget(self)
        self.setCentralWidget(self.main)
        self.table = QTableWidget()
        self.table.setColumnCount(10)


        self.table.setRowCount(10)
        #self.table.setRowHeight(230, 35)
        #self.table.setModel(QAbstractItemModel)
        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        vbox.addStretch()
        self.main.setLayout(vbox)

    def employee_details(self):
        dept = self.dept.currentText()
        fname=self.first_name.text()
        self.first_name.setText("")
        lname=self.last_name.text()
        self.last_name.setText("")
        name = fname + " " +lname
        DOB = self.dob.text()
        GENDER = self.gender.currentText()
        self.gender.setCurrentText("Gender")
        user = self.username.text()
        self.username.setText("")
        passw = self.password.text()
        self.password.setText("")

        items = (dept,name,DOB,GENDER,user,passw)

        query = """INSERT INTO Employees(Department,emp_name,dob,gender,usernames,passwords) VALUES (%s,%s,%s,%s,%s,%s)"""
        try:
            mydb.execute(query, items)
            db.commit()
            self.mbox = QMessageBox.information(self, 'Alert', 'Successfully added')

        except:
            self.mbox = QMessageBox.information(self, 'Alert', 'Unable to add!!Please try again')






    def logout(self,events):
        self.log = Login.Login()
        self.log.show()
        self.close()




    def clicked(self):
         print("clicked")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    admin = Admin()
    admin.show()
    sys.exit(app.exec_())
