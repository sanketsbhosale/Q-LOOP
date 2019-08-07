
from PyQt5 import QtCore, QtGui, QtWidgets
from PMS import Ui_MainWindow
from Forgot_Password import Ui_Forgot_Password
from Sign_up111 import Ui_New_user
import sqlite3

class Ui_Login_Form(object):

    def openPMS(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def onClickLoginTable(self):
        try:
            self.loginTable()
        except TypeError:
            self.showMessageBox("Login Form ","User Not Found!")
        except:
            self.showMessageBox("Login Form","Error in Logging !")

    def loginTable(self):

        username=str(self.lineEdit.text())
        password=str(self.lineEdit_2.text())

        if(len(username) == 0 and \
             len(password) == 0):
            self.showMessageBox("Login Form","Please Enter Username and Password!")

        elif(len(password) == 0 ):
            self.showMessageBox("Login Form","Please Enter Password!")

        elif(len(username) == 0 ):
            self.showMessageBox("Login Form","Please Enter Username!")

        else:
            connection=sqlite3.connect("loginDB.db")
            c=connection.cursor()
            result=connection.execute("SELECT * FROM LoginDBTable")
            connection.commit()
            for row in connection.fetchall():
                    print(row)
                    username1 = row[0]
                    password1 = row[2]
                    print("username: " + row[0])
                    print("email   : " + row[1])
                    print("password: " + row[2])
                    
                    if (username == username1 and \
                        password == password1):
                        self.openPMS()
                            
                    else:
                        self.showMessageBox("Login Form","Please Enter Username and Password!")
        c.close()
        connection.close()

    def openNew_User(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_New_user()
        self.ui.setupUi(self.window)
        self.window.show()

    def openForgot_Pass(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Forgot_Password()
        self.ui.setupUi(self.window)
        self.window.show()

    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Login_Form):
        Login_Form.setObjectName("Login_Form")
        Login_Form.resize(731, 399)
        Login_Form.setMinimumSize(QtCore.QSize(731, 399))
        Login_Form.setMaximumSize(QtCore.QSize(731, 399))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login_Form.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(Login_Form)
        self.centralwidget.setObjectName("centralwidget")

        ###################### Labels ###################################
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 130, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 200, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        ####################### LineEdit ###############################
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 151, 271, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 222, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        ########################### Buttons #########################
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 300, 180, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClickLoginTable)

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(530, 222, 111, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.openForgot_Pass)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 300, 171, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openNew_User)

        Login_Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_Form)
        QtCore.QMetaObject.connectSlotsByName(Login_Form)

    def retranslateUi(self, Login_Form):
        _translate = QtCore.QCoreApplication.translate
        Login_Form.setWindowTitle(_translate("Login_Form", "Login Form"))
        self.label.setText(_translate("Login_Form", "Username :"))
        self.label_2.setText(_translate("Login_Form", "Password :"))
        self.pushButton.setText(_translate("Login_Form", "View User"))
        self.label_3.setText(_translate("Login_Form", "LOGIN FORM"))
        self.toolButton.setText(_translate("Login_Form", "Forgot Password"))
        self.pushButton_2.setText(_translate("Login_Form", "New User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Form = QtWidgets.QMainWindow()
    ui = Ui_Login_Form()
    ui.setupUi(Login_Form)
    Login_Form.show()
    sys.exit(app.exec_())

