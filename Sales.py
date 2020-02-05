import mysql.connector
import Login
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *

db = mysql.connector.connect(user='root', password='Vipin@123',
                              host='127.0.0.1',
                              database='NETaxi')
mydb = db.cursor()

class Sales(QMainWindow):

    def __init__(self):
        super(Sales, self).__init__()
        self.bar = self.menuBar()
        file = self.bar.addMenu("File")
        file.addAction("New")
        file.addAction("Save")
        file.addAction("Copy")
        file.addAction("Paste")
        file.addAction("Quit")
        edit = self.bar.addMenu("Edit")
        view = self.bar.addMenu("View")
        help = self.bar.addMenu("Help")
        help.addAction("About us")
        help.addAction("Logout")

        self.title = self.setWindowTitle("Sales Department")
        self.setGeometry(50, 70, 1800, 950)
        self.setWindowIcon(QtGui.QIcon("Window_icon.jpg"))

        self.toolbar = QToolBar()
        self.toolbar.setStyleSheet("width:180px; height: 70px")
        self.toolbar.setMovable(False)

        self.Info = QtWidgets.QToolButton()
        self.Info.setText(" Packages Info")
        self.Info.setStyleSheet("margin-left: 5px; margin-right: 2px;background-color: #cbcbb3;font-size: 18px;")
        self.Info.setToolTip("<p>For Packages and offerings</p>")
        self.Info.clicked.connect(self.info)


        self.Create_Itinerary = QtWidgets.QToolButton()
        self.Create_Itinerary.setText("Create Itinerary")
        self.Create_Itinerary.setToolTip("<h5>To create new packages</h5>")
        self.Create_Itinerary.setStyleSheet("margin-right: 2px;background-color: #cbcbb3;font-size: 18px;")
        self.Create_Itinerary.clicked.connect(self.Itinerary)


        self.Booked_package = QtWidgets.QToolButton()
        self.Booked_package.setText("Package Confirmed")
        self.Booked_package.setStyleSheet("margin-right: 2px;background-color: #cbcbb3; font-size: 18px;")
        self.Booked_package.setToolTip("<p>Confirmed from Sales</p>")
        self.Booked_package.clicked.connect(self.packages)

        self.Logout = QtWidgets.QToolButton()
        self.Logout.setText("Logout")
        self.Logout.setStyleSheet("margin-right: 2px;background-color: #cbcbb3;font-size: 18px;")
        self.Logout.setToolTip("<p>For account related documents</p>")
        self.Logout.clicked.connect(self.logout)

        self.toolbar.addWidget(self.Info)
        self.toolbar.addWidget(self.Create_Itinerary)
        self.toolbar.addWidget(self.Booked_package)
        self.toolbar.addWidget(self.Logout)
        self.addToolBar(self.toolbar)

        self.copyright = QLabel("© NE Taxi 2019. All Rights Reserved.",self)
        self.copyright.setStyleSheet(" color: black;  background-color: white; font-size: 15px;   ")
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.addPermanentWidget(self.copyright,50)

    def info(self):

        self.main = QWidget(self)
        self.setCentralWidget(self.main)

        topleft = QtWidgets.QFrame()
        topleft.setFixedWidth(300)
        topleft.setFrameShape(QtWidgets.QFrame.StyledPanel)

        vbox = QVBoxLayout()
        treeWidget = QtWidgets.QTreeWidget()
        treeWidget.setHeaderLabel("All Packages")
        treeWidget.setWindowModality(QtCore.Qt.WindowModal)

        self.topLevelItem1 = QtWidgets.QTreeWidgetItem()
        self.topLevelItem1.setText(0, "Sikkim and Darjeeling")

        self.topLevelItem2 = QtWidgets.QTreeWidgetItem()
        self.topLevelItem2.setText(0, "Rest of NE")

        self.topLevelItem3 = QtWidgets.QTreeWidgetItem()
        self.topLevelItem3.setText(0, "Bhutan")

        treeWidget.addTopLevelItems([self.topLevelItem1, self.topLevelItem2, self.topLevelItem3])

        # Sikkim and Darjeeling Pacakages
        self.Gangtok = QtWidgets.QLabel("Gangtok")
        self.Lachen = QtWidgets.QLabel("Lachen")
        self.Lachung = QtWidgets.QLabel("Lachung")
        self.Kalimpong = QtWidgets.QLabel("Kalimpong")
        self.Namchi_Ravangla = QtWidgets.QLabel("Namchi & Ravangla")
        self.Pelling = QtWidgets.QLabel("Pelling")
        self.Darjeeling = QtWidgets.QLabel("Darjeeling")

        self.childItems = []
        for i in range(7):
            self.childItems.append(QtWidgets.QTreeWidgetItem())
            self.topLevelItem1.addChild(self.childItems[i])
        treeWidget.setItemWidget(self.childItems[0], 0, self.Gangtok)
        treeWidget.setItemWidget(self.childItems[1], 0, self.Lachen)
        treeWidget.setItemWidget(self.childItems[2], 0, self.Lachung)
        treeWidget.setItemWidget(self.childItems[3], 0, self.Kalimpong)
        treeWidget.setItemWidget(self.childItems[4], 0, self.Namchi_Ravangla)
        treeWidget.setItemWidget(self.childItems[5], 0, self.Pelling)
        treeWidget.setItemWidget(self.childItems[6], 0, self.Darjeeling)

        # Rest of NE Packages
        self.Bomdila = QtWidgets.QLabel("Bomdila")
        self.Tawang = QtWidgets.QLabel("Tawang")
        self.Dirang = QtWidgets.QLabel("Dirang")
        self.Bhalukpong = QtWidgets.QLabel("Bhalupong")
        self.Kaziranga = QtWidgets.QLabel("Kaziranga")
        self.Guwahati = QtWidgets.QLabel("Guwahati")
        self.Shillong = QtWidgets.QLabel("Shillong")
        self.Cherapunjee = QtWidgets.QLabel("Cherapunjee")
        self.Majuli = QtWidgets.QLabel("Majuli")
        self.Sibsagar = QtWidgets.QLabel("Sibsagar")
        self.Mawlynnong = QtWidgets.QLabel("Mawlynnong")

        self.childItems1 = []
        for i in range(11):
            self.childItems1.append(QtWidgets.QTreeWidgetItem())
            self.topLevelItem2.addChild(self.childItems1[i])

        treeWidget.setItemWidget(self.childItems1[0], 0, self.Bomdila)
        treeWidget.setItemWidget(self.childItems1[1], 0, self.Tawang)
        treeWidget.setItemWidget(self.childItems1[2], 0, self.Dirang)
        treeWidget.setItemWidget(self.childItems1[3], 0, self.Bhalukpong)
        treeWidget.setItemWidget(self.childItems1[4], 0, self.Kaziranga)
        treeWidget.setItemWidget(self.childItems1[5], 0, self.Guwahati)
        treeWidget.setItemWidget(self.childItems1[6], 0, self.Shillong)
        treeWidget.setItemWidget(self.childItems1[7], 0, self.Cherapunjee)
        treeWidget.setItemWidget(self.childItems1[8], 0, self.Majuli)
        treeWidget.setItemWidget(self.childItems1[9], 0, self.Sibsagar)
        treeWidget.setItemWidget(self.childItems1[10], 0, self.Mawlynnong)

        # Bhutan Packages
        self.Paro = QtWidgets.QLabel("Paro")
        self.Thimphu = QtWidgets.QLabel("Thimphu")
        self.Punakha = QtWidgets.QLabel("Punakha")
        self.Bumthang = QtWidgets.QLabel("Bumthang")

        self.childItems2 = []
        for i in range(4):
            self.childItems2.append(QtWidgets.QTreeWidgetItem())
            self.topLevelItem3.addChild(self.childItems2[i])

        treeWidget.setItemWidget(self.childItems2[0], 0, self.Paro)
        treeWidget.setItemWidget(self.childItems2[1], 0, self.Thimphu)
        treeWidget.setItemWidget(self.childItems2[2], 0, self.Punakha)
        treeWidget.setItemWidget(self.childItems2[3], 0, self.Bumthang)

        vbox.addWidget(treeWidget)
        topleft.setLayout(vbox)

        self.topright = QtWidgets.QFrame()
        self.topright.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.lebel = QLabel()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.lebel)
        self.topright.setLayout(vbox1)



        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)

        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(self.scroll)

        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter1)
        self.main.setLayout(hbox)
        self.Guwahati.mouseReleaseEvent = self.row

    def row(self,events):
        for i in range(len(self.topright.children())):
            self.topright.children()[i].deleteLater()

        self.frame1 = QFrame()
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFixedHeight(100)
        self.frame2 = QFrame()
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFixedHeight(100)
        self.frame3 = QFrame()
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFixedHeight(300)
        self.frame4 = QFrame()
        self.frame4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame4.setFixedHeight(300)
        self.frame5 = QFrame()
        self.frame5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame5.setFixedHeight(300)

        vbox = QVBoxLayout()
        reg = QLabel("")
        place = QLabel("")
        sight = QLabel("")
        out = QLabel("")
        cos = QLabel("")
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()

        mydb.execute("SELECT * FROM Place")
        for row in mydb:

            if(row[1] == "Guwahati"):
                reg.setText(row[0])
                place.setText(row[1])
                sight.setText(row[2])
                out.setText(row[3])
                cos.setText(row[4])

                hbox1.addWidget(reg)
                hbox2.addWidget(place)
                hbox3.addWidget(sight)
                hbox4.addWidget(out)
                hbox5.addWidget(cos)
                self.frame1.setLayout(hbox1)
                self.frame2.setLayout(hbox2)
                self.frame3.setLayout(hbox3)
                self.frame4.setLayout(hbox4)
                self.frame5.setLayout(hbox5)
                vbox.addWidget(self.frame1)
                vbox.addWidget(self.frame2)
                vbox.addWidget(self.frame3)
                vbox.addWidget(self.frame4)
                vbox.addWidget(self.frame5)
                self.topright.setLayout(vbox)

                self.scroll.setWidget(self.topright)

    def Itinerary(self):
        self.main = QWidget(self)
        self.setCentralWidget(self.main)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.leftframe = QFrame()
        self.leftframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftframe.setFixedWidth(500)
        self.rightframe_up = QFrame()
        self.rightframe_up.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightframe_up.setFixedHeight(100)
        self.rightframe_down = QFrame()
        self.rightframe_down.setFrameShape(QtWidgets.QFrame.StyledPanel)


        vbox = QVBoxLayout()
        vbox.addWidget(self.rightframe_up)
        vbox.addWidget(self.scroll)

        self.formiti2 = QFormLayout()
        self.fram = QFrame()
        self.fram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fram.setFixedHeight(600)
        self.formiti2.addRow("",QLabel("D1"))
        self.formiti2.addRow("", QLabel("D2"))
        self.formiti2.addRow("", QLabel("D3"))
        self.formiti2.addRow("", QLabel("D4"))
        self.formiti2.addRow("", QLabel("D5"))
        self.formiti2.addRow("", QLabel("D6"))
        self.formiti2.addRow("", QLabel("D7"))
        self.formiti2.addRow("", QLabel("D8"))
        self.formiti2.addRow("", QLabel("D9"))
        self.formiti2.addRow("", QLabel("D10"))




        self.formiti1 = QFormLayout()


        hb = QHBoxLayout()
        hb.addLayout(self.formiti2)
        hb.addLayout(self.formiti1)
        self.fram.setLayout(hb)

        self.Create_Package = QPushButton()
        self.Create_Package.setText("Create Packages")
        self.Create_Package.setStyleSheet("margin-right: 2px;background-color: #cbcbb3;font-size: 18px;")
        self.Create_Package.clicked.connect(self.create_packages)

        fo = QFormLayout()
        leb = QLabel("Packages Selected")
        leb.setAlignment(QtCore.Qt.AlignCenter)
        fo.addRow("",leb)
        fo.addRow("",self.fram)
        fo.addRow("",self.Create_Package)
        self.leftframe.setLayout(fo)

        #for j in range(len(self.leftframe.children())):
         #   self.formiti2.addRow("", QLabel(str(j+1)))





        self.text1 = QComboBox()
        self.text1.addItems(['Pickup Location','Bagdogra','Gangtok','Lachen','Darjeeling','Ravangla','Kalimpong'])
        self.text1.setStyleSheet("font-size:15px")
        self.text1.setFixedWidth(300)
        self.text1.setFixedHeight(35)

        self.text2 = QComboBox()
        self.text2.addItems(['Destination','Gangtok','Lachen','Lachung','Kalimpong','Ravangla via Namchi','Pelling','Darjeeling'])
        self.text2.setStyleSheet("font-size:15px")
        self.text2.setFixedWidth(300)
        self.text2.setFixedHeight(35)

        self.btn = QPushButton("Query")
        self.btn.setStyleSheet("font-size:18px")
        self.btn.setFixedHeight(40)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.text1)
        hbox1.addWidget(self.text2)
        hbox1.addWidget(self.btn)
        hbox1.addStretch()
        self.rightframe_up.setLayout(hbox1)
        hbox = QHBoxLayout()
        hbox.addWidget(self.leftframe)
        hbox.addLayout(vbox)
        self.main.setLayout(hbox)
        self.btn.clicked.connect(self.Gang)

    def Gang(self):

        pickup = self.text1.currentText()
        dest = self.text2.currentText()
        form = QFormLayout()
        day = QLabel("Days")
        day.setFixedWidth(50)
        day.setStyleSheet(" background-color:#fab436;font-size:15px;font-weight:bold;")
        pick = QLabel("Pickup Location")
        pick.setFixedWidth(150)
        pick.setFixedHeight(40)
        pick.setStyleSheet("background-color:#fab436;font-size:15px;font-weight:bold;")
        desti = QLabel("Destination")
        desti.setFixedWidth(200)
        desti.setFixedHeight(40)
        desti.setStyleSheet("text-align:center;background-color:#fab436;font-size:15px;font-weight:bold;")
        out = QLabel("Outstation")
        out.setFixedWidth(300)
        out.setFixedHeight(40)
        out.setStyleSheet("background-color:#fab436;font-size:15px;font-weight:bold;")
        sight = QLabel("SightSeen")
        sight.setFixedHeight(40)
        sight.setFixedWidth(500)
        #sight.setFixedWidth(300)
        sight.setStyleSheet("background-color:#fab436;font-size:15px;font-weight:bold;")
        cost = QLabel("Cost")
        cost.setFixedHeight(40)
        cost.setStyleSheet("background-color:#fab436;font-size:15px;font-weight:bold;text-align:center")
        hbox3 = QHBoxLayout()
        hbox3.addWidget(day)
        hbox3.addWidget(pick)
        hbox3.addWidget(desti)
        hbox3.addWidget(out)
        hbox3.addWidget(sight)

        hbox3.setAlignment(QtCore.Qt.AlignTop)
        form.addRow("",hbox3)



        #form1 = QFormLayout()
        #form2 = QFormLayout()
        for i in range(len(self.rightframe_down.children())):
            self.rightframe_down.children()[i].deleteLater()
        i=1
        self.lebel6 = [30]
        self.lebel2 = [30]
        self.lebel3 = [30]
        self.lebel4 = [30]
        self.lebel5 = [30]
        frame = [30]
        mydb.execute("SELECT * FROM Sikkim_Pack")
        for row in mydb:
            if((row[1] == pickup or row[2] == pickup or row[3] == pickup or row[4] == pickup or row[5] == pickup ) and row[6] == dest):
                frame.append(i)
                self.lebel2.append(i)
                self.lebel3.append(i)
                self.lebel4.append(i)
                self.lebel5.append(i)
                frame[i] = QFrame()
                self.hbox2 = QHBoxLayout()
                self.lebel1 = QLabel(row[7])
                self.lebel1.setFixedWidth(80)
                self.lebel2[i] = QLabel(row[8])
                self.lebel2[i].setFixedWidth(150)
                self.lebel3[i] = QLabel(row[9])
                self.lebel3[i].setFixedWidth(200)
                self.lebel4[i] = QLabel(row[10])
                self.lebel4[i].setFixedWidth(350)
                self.lebel5[i] = QLabel(row[11])
                self.lebel5[i].setFixedWidth(400)
                self.lebel6.append(i)
                self.lebel6[i] = QPushButton("Add")
                self.hbox2.addWidget(self.lebel1)
                self.hbox2.addWidget(self.lebel2[i])
                self.hbox2.addWidget(self.lebel3[i])
                self.hbox2.addWidget(self.lebel4[i])
                self.hbox2.addWidget(self.lebel5[i])
                self.hbox2.addWidget(self.lebel6[i])
                frame[i].setLayout(self.hbox2)
                frame[i].setFixedHeight(100)
                frame[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
                form.addRow("",frame[i])
                i=i+1
        if(dest == "Gangtok" and pickup == 'Bagdogra'):


            self.lebel6[1].clicked.connect(lambda a: self.formiti1.addRow("",QLabel("Bagdogra to Gaangtok")))
            self.lebel6[2].clicked.connect(lambda a: self.formiti1.addRow("",QLabel("Lachung to Gaangtok")))
            self.lebel6[3].clicked.connect(lambda a: self.formiti1.addRow("",QLabel("Lachen to Gaangtok")))
            self.lebel6[4].clicked.connect(lambda a: self.formiti1.addRow("",QLabel("Kalimpong to Gaangtok")))
            self.lebel6[5].clicked.connect(lambda a: self.formiti1.addRow("",QLabel("Darjeeling to Gaangtok")))
            self.lebel6[6].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Full day mandir and Lake Sightseen")))
            self.lebel6[7].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("")))
            self.lebel6[8].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[9].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[10].clicked.connect(lambda a: self.formiti1.addRow("",QLabel("Bagdogra to Gaangtok") ))
            self.lebel6[11].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[12].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[13].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[14].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[15].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[16].clicked.connect(lambda a: self.formiti1.addRow("",QLabel("Bagdogra to Gaangtok")))
            self.lebel6[17].clicked.connect(lambda a: self.formiti1.addRow("",QLabel("Bagdogra to Gaangtok")))
            self.lebel6[18].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[19].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[20].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))
            self.lebel6[21].clicked.connect(lambda a: self.formiti1.addRow("", QLabel("Bagdogra to Gaangtok")))








        self.rightframe_down.setLayout(form)
        self.scroll.setWidget(self.rightframe_down)

    def create_packages(self):

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QtWidgets.QFormLayout()
        hbox = QHBoxLayout()
        firstName = QLineEdit()
        firstName.setPlaceholderText("First Name")
        lastName = QLineEdit()
        lastName.setPlaceholderText("Last Name")
        hbox.addWidget(firstName)
        hbox.addWidget(lastName)
        layout.setSpacing(30)
        layout.setContentsMargins(220,100,250,40)
        self.heading = QLabel("Traveller Details",self)
        self.heading.setStyleSheet("font-size: 20px;")
        layout.addWidget(self.heading)
        layout.addRow("Name",hbox)

        hbox1 = QHBoxLayout()
        age = QLineEdit()
        age.setPlaceholderText("Enter age in years")
        self.gender = QComboBox()
        self.gender.addItems(["Select","Male", "Female" , "Other" ])
        hbox1.addWidget(self.gender)

        hbox1.addWidget(age)
        layout.addRow("Gender", hbox1)

        layout.addRow("Email Address", QLineEdit())
        layout.addRow("Mobile Number", QLineEdit())
        layout.addRow("Enter Pickup location", QLineEdit())
        self.package_sel = QComboBox()
        self.package_sel.addItems(["", "", ""])
        layout.addRow("Package Selected", self.package_sel )
        layout.addRow("Cost", QLineEdit())

        submit = QPushButton("Submit",self)
        clear = QPushButton("Clear",self)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(submit)
        hbox2.addWidget(clear)
        hbox2.setContentsMargins(270,60,250,0)
        layout.addRow(hbox2)
        self.main_widget.setLayout(layout)

    def packages(self):
        pass

    def account(self):
        pass

    def acc(self):
        pass

    def logout(self):
        self.log = Login.Login()
        self.log.show()
        self.close()


    def clicked(self):
         print("clicked")

class Database():

    def __init__(self):
        pass
    def creatDatabase(self):
        pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    sales = Sales()
    sales.show()
    sys.exit(app.exec_())

