
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import validators

class Ui_New_user(object):

    def onClickSignUp(self):
        try:
            self.signUpDB()
        except sqlite3.IntegrityError:
            self.showWMessageBox("Sign Up","User Exist!")
        except:
            self.showWMessageBox("Sign Up","User Exist!")

    def signUpDB(self):

        username=str(self.lineEdit_2.text())
        email=str(self.lineEdit_3.text())
        password=str(self.lineEdit_4.text())
        QID=str(self.lineEdit_5.text())

        #ve=validators.email(email)

        if(QID == "21345"):
            if(len(username) == 0 and \
                len(email) == 0 and \
                len(password) == 0):
                self.showWMessageBox("Sign Up","Please Enter all Details!")
                
            elif(len(username) == 0 and \
               len(email) == 0):
               self.showWMessageBox("Sign Up","Please Enter all Details!")

            elif(len(username) == 0 and \
               len(Password) == 0):
               self.showWMessageBox("Sign Up","Please Enter all Details!")

            elif(len(email) == 0 and \
               len(password) == 0):
               self.showWMessageBox("Sign Up","Please Enter all Details!")

            elif(len(username) == 0 ):
               self.showWMessageBox("Sign Up","Please Enter all Details!")

            elif(len(email) == 0):
               self.showWMessageBox("Sign Up","Please Enter all Details!")

            elif(len(password) == 0):
               self.showWMessageBox("Sign Up","Please Enter all Details!")

            else:
                connection=sqlite3.connect("loginDB.db")
                c=connection.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS LoginDBTable(USERNAME TEXT NOT NULL PRIMARY KEY, EMAIL TEXT NOT NULL, PASSWORD TEXT NOT NULL)")
                c.execute("INSERT INTO LoginDBTable VALUES(?,?,?)",(username,email,password))
                connection.commit()
                result=c.execute("SELECT * FROM LoginDBTable WHERE USERNAME=?",(username,))
                for row in c.fetchall():
                    print("username: " + row[0])
                    print("email   : " + row[1])
                    print("password: " + row[2])
                c.close()
                connection.close()

                self.showRMessageBox("Sign Up","Submitted Successfully!")
        else:
            self.showWMessageBox("Sign Up","Please Enter the Valid QID!")
         
    def showWMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showRMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, New_user):
        New_user.setObjectName("New_user")
        New_user.resize(786, 488)
        New_user.setMinimumSize(QtCore.QSize(786, 488))
        New_user.setMaximumSize(QtCore.QSize(786, 488))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        New_user.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(New_user)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 211, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 410, 171, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.onClickSignUp
                                          )

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 30, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 272, 271, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 250, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 190, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 310, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 334, 271, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 150, 271, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(160, 130, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        New_user.setCentralWidget(self.centralwidget)

        self.retranslateUi(New_user)
        QtCore.QMetaObject.connectSlotsByName(New_user)

    def retranslateUi(self, New_user):
        _translate = QtCore.QCoreApplication.translate
        New_user.setWindowTitle(_translate("New_user", "Create New User"))
        self.pushButton_2.setText(_translate("New_user", "Sign up"))
        self.label_5.setText(_translate("New_user", "Create New User"))
        self.label_6.setText(_translate("New_user", "Email ID :"))
        self.label_7.setText(_translate("New_user", "Username :"))
        self.label_8.setText(_translate("New_user", "Password :"))
        self.label_9.setText(_translate("New_user", "QID :"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_user = QtWidgets.QMainWindow()
    ui = Ui_New_user()
    ui.setupUi(New_user)
    New_user.show()
    sys.exit(app.exec_())
