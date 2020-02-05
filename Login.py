import mysql.connector
import Sales
import Admin
import Operation
import Accountant
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
cnx = mysql.connector.connect(user='root', password='Vipin@123',
                              host='127.0.0.1',
                              database='NETaxi')
cursor=cnx.cursor()

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Portal")
        self.setWindowIcon(QIcon("C:/Users/Dhrubajit Sarkar/Desktop/ne-logo.png"))
        self.setGeometry(650,250,500,500)
        self.setFixedHeight(600)
        self.setFixedWidth(640)
        self.UI()
    def UI(self):
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap("lebel_icon.jpg"))
        self.logo.setFixedWidth(630)
        self.logo.setFixedHeight(120)
        self.logo.move(3,3)
        self.logo.setStyleSheet("margin:0px;padding:0px;")
        lebel = QLabel("Department",self)
        lebel.move(65, 150)
        lebel.setStyleSheet("font-size:18px;font-family:sans-serif;")
        #lebel.setStyleSheet("font-weight:bold; font-size:px; font-family:sans-serif")
        self.combobox = QComboBox(self)
        self.combobox.addItems(["Select","Sales", "Accounts","Operation","Admin"])
        self.combobox.setCurrentText("Select")

        self.combobox.setFixedHeight(40)
        self.combobox.setFixedWidth(500)
        self.combobox.move(65,180)
        self.combobox.setStyleSheet("font-size:16px;")
        lebel_username = QLabel("Username", self)
        lebel_username.setStyleSheet("font-size:18px;font-family:sans-serif;")
        lebel_username.move(65, 240)
        frame_username = QFrame(self)
        frame_username.setFrameShape(QFrame.StyledPanel)
        frame_username.setFixedWidth(500)
        frame_username.setFixedHeight(40)
        frame_username.move(65,270)
        image_username = QLabel(frame_username)
        image_username.setPixmap(QPixmap("user.png").scaled(20,20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        image_username.move(10,4)
        self.textbox1 = QLineEdit(frame_username)
        self.textbox1.setFrame(False)
        self.textbox1.setPlaceholderText("Enter Username")
        self.textbox1.setStyleSheet("font-size:16px;")
        self.textbox1.setTextMargins(8, 0, 4, 1)
        self.textbox1.setFixedWidth(500)
        self.textbox1.setFixedHeight(40)
        self.textbox1.move(40,1)

        lebel_password = QLabel("Password", self)
        lebel_password.setStyleSheet("font-size:18px;font-family:sans-serif;")
        lebel_password.move(65, 330)
        frame_password = QFrame(self)
        frame_password.setFrameShape(QFrame.StyledPanel)
        frame_password.setFixedWidth(500)
        frame_password.setFixedHeight(35)
        frame_password.move(65, 360)
        image_password = QLabel(frame_password)
        image_password.setPixmap(
            QPixmap("pass.jpg").scaled(20, 20, Qt.KeepAspectRatio,
                                                                             Qt.SmoothTransformation))
        image_password.move(10, 4)
        self.textbox2 = QLineEdit(frame_password)
        self.textbox2.setFrame(False)
        self.textbox2.setPlaceholderText("Enter Password")
        self.textbox2.setEchoMode(QLineEdit.Password)

        self.textbox2.setStyleSheet("font-size:16px;")
        self.textbox2.setTextMargins(8, 0, 4, 1)
        self.textbox2.setFixedWidth(500)
        self.textbox2.setFixedHeight(35)
        self.textbox2.move(40, 1)

        self.radiobtn = QRadioButton(self)
        self.radiobtn.setText("Show Password")
        self.radiobtn.setStyleSheet("font-size:15px;")
        self.radiobtn.move(75,410)
        self.radiobtn.setChecked(False)
        self.radiobtn.toggled.connect(self.show_pass)




        self.enterButton = QPushButton("Login", self)
        self.enterButton.move(85,460)
        #self.enterButton.resize(100,40)
        self.enterButton.setStyleSheet("width:200px;height:35px;font-size:18px;")
        self.enterButton.clicked.connect(self.newWindow)

        self.clearButton = QPushButton("Clear", self)
        self.clearButton.move(325,460)
        #self.enterButton.resize(100,40)
        self.clearButton.setStyleSheet("width:200px;height:35px;font-size:18px;")
        self.clearButton.clicked.connect(self.clear)


    def show_pass(self):
        self.radiobtn = self.sender()
        if self.radiobtn.isChecked():
            self.textbox2.setEchoMode(QLineEdit.Normal)
        else:
            self.textbox2.setEchoMode(QLineEdit.Password)



    def hide(self):
        self.destroy()


    def newWindow(self):
        user = self.textbox1.text()
        passw = self.textbox2.text()
        p = 0


        cursor.execute("SELECT * FROM Employees")
        result = cursor.fetchall()

        if(self.combobox.currentText() == "Sales"):
            for row in result:
                if (row[0] == "Sales"):

                    if (user == row[5] and passw == row[6]):
                        self.sales = Sales.Sales()
                        self.sales.show()
                        self.destroy()



        if (self.combobox.currentText() == "Accounts"):
            for row in result:
                if (row[0] == "Accounts"):

                    if (user == row[5] and passw == row[6]):
                        self.ui = Accountant.Window()
                        self.ui.show()
                        self.close()

        if (self.combobox.currentText() == "Operation"):
            for row in result:
                if (row[0] == "Operation"):

                    if (user == row[5] and passw == row[6]):
                        self.ui = Operation.Operation()
                        self.ui.show()
                        self.close()

        if (self.combobox.currentText() == "Admin"):
            for row in result:
                if (row[0] == "Admin"):

                    if (user == row[5] and passw == row[6]):
                        self.ui = Admin.Admin()
                        self.ui.show()
                        self.close()

        if(self.combobox.currentText() == "Select"):
            self.mbox = QMessageBox.information(self, 'Alert', 'Please Select Department')


        if (self.combobox.currentText() == result[0]):
             if(user !=result[5] or passw !=result[6]):
                self.mbox = QMessageBox.information(self, 'Alert', 'Incorrect Combination')






    def clear(self):
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.combobox.setCurrentText("Select")



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    log = Login()
    log.show()
    sys.exit(app.exec_())
