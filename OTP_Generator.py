
from PyQt5 import QtCore, QtGui, QtWidgets
import pyotp
import validators

class Ui_OTP_Gen(object):

    def onClickCreate(self):
        try:
            self.create()
        except IOError:
            self.showMessageBox("OTP Genrator","!")

    def create(self):
        username=str(self.lineEdit.text())
        email=str(self.lineEdit_2.text())
        phone_no=str(self.lineEdit_3.text())

        ######################## Validation #############################
        ve=validators.email(email)
        vpn=validators.length(phone_no, min=10, max=10)

        if (len(username) == 0 and \
            len(email) == 0 and \
            len(phone_no) == 0):
            self.showMessageBox("OTP Genrator","Please Enter All Details")

        elif (len(username) == 0 and \
            len(email) == 0 ):
            self.showMessageBox("OTP Genrator","Please Enter All Details")

        elif (len(username) == 0):
            self.showMessageBox("OTP Genrator","Please Enter All Details")

        elif (len(email) == 0):
            self.showMessageBox("OTP Genrator","Please Enter All Details")

        elif ve is True:
            OTP=pyotp.random_base32()
            totp = pyotp.TOTP(OTP)
            pyotp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(email, issuer_name=username)
            OP=("Current OTP: ", totp.now())

            if vpn is True:
                self.showRMessageBox("OTP GENERATOR","".join(OP))
            else:
                self.showMessageBox("OTP Genrator","Invalid Mobile No.!")

        else:
            self.showMessageBox("OTP Genrator","Invalid Email !")

    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showRMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, OTP_Gen):
        OTP_Gen.setObjectName("OTP_Gen")
        OTP_Gen.resize(860, 505)
        OTP_Gen.setMinimumSize(QtCore.QSize(860, 505))
        OTP_Gen.setMaximumSize(QtCore.QSize(860, 505))
        self.centralwidget = QtWidgets.QWidget(OTP_Gen)
        self.centralwidget.setObjectName("centralwidget")

        ##################### Label ###################

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 139, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 210, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 281, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 50, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        ######################## LineEdit ######################

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(420, 160, 271, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 231, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 302, 271, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        ########################### Button ##########################

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 380, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClickCreate)

        OTP_Gen.setCentralWidget(self.centralwidget)

        self.retranslateUi(OTP_Gen)
        QtCore.QMetaObject.connectSlotsByName(OTP_Gen)

    def retranslateUi(self, OTP_Gen):
        _translate = QtCore.QCoreApplication.translate
        OTP_Gen.setWindowTitle(_translate("OTP_Gen", "MainWindow"))
        self.pushButton.setText(_translate("OTP_Gen", "Generate OTP !"))
        self.label.setText(_translate("OTP_Gen", "Username :"))
        self.label_2.setText(_translate("OTP_Gen", "Email ID:"))
        self.label_3.setText(_translate("OTP_Gen", "Phone Number :"))
        self.label_4.setText(_translate("OTP_Gen", "OTP Generater"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OTP_Gen = QtWidgets.QMainWindow()
    ui = Ui_OTP_Gen()
    ui.setupUi(OTP_Gen)
    OTP_Gen.show()
    sys.exit(app.exec_())

