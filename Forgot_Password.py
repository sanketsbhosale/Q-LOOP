
from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
import sqlite3
from smtplib import SMTPRecipientsRefused

class Ui_Forgot_Password(object):

    def sendMail(self):
        global a,b,c

        entered_Email=str(self.lineEdit.text())
        #entered_Email="sanketsbhosale2016@gmail.com"
        connection=sqlite3.connect("loginDB.db")
        c=connection.cursor()
        
        result=c.execute("SELECT * FROM LoginDBTable WHERE EMAIL=?",(entered_Email,))
        for row in c.fetchall():
            print("username: " + row[0])
            print("email   : " + row[1])
            print("password: " + row[2])

        conn=smtplib.SMTP('smtp.gmail.com',587)
        conn.ehlo()
        conn.starttls()
        conn.login('123sampleusers123@gmail.com','sample456')
        conn.sendmail('123sampleusers123@gmail.com',entered_Email,"Your Password is " + row[2] )
        conn.quit()
        
        self.showMessageBox("Forgot Password","Your Password is " + row[2] )

        connection.close()

    def onClickSendMail(self):
        try:
            self.sendMail()
        except smtplib.SMTPRecipientsRefused:
            self.showWMessageBox("Forgot Password","Email Doesn't match !")
        except UnboundLocalError:
            self.showWMessageBox("Forgot Password","Error - Entered Email is invalid !")
        except:
            self.showWMessageBox("Forgot Password","Enter Valid Email !")
        
    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showWMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    
    def setupUi(self, Forgot_Password):
        Forgot_Password.setObjectName("Forgot_Password")
        Forgot_Password.resize(801, 312)
        Forgot_Password.setMinimumSize(QtCore.QSize(801, 312))
        Forgot_Password.setMaximumSize(QtCore.QSize(801, 312))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Forgot_Password.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(Forgot_Password)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 151, 311, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 50, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 220, 180, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClickSendMail)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 130, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Forgot_Password.setCentralWidget(self.centralwidget)

        self.retranslateUi(Forgot_Password)
        QtCore.QMetaObject.connectSlotsByName(Forgot_Password)

    def retranslateUi(self, Forgot_Password):
        _translate = QtCore.QCoreApplication.translate
        Forgot_Password.setWindowTitle(_translate("Forgot_Password", "Forgot_Password"))
        self.label_3.setText(_translate("Forgot_Password", "Forgot Password"))
        self.pushButton.setText(_translate("Forgot_Password", "Forgot Password >"))
        self.label.setText(_translate("Forgot_Password", "Email ID :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Forgot_Password = QtWidgets.QMainWindow()
    ui = Ui_Forgot_Password()
    ui.setupUi(Forgot_Password)
    Forgot_Password.show()
    sys.exit(app.exec_())

