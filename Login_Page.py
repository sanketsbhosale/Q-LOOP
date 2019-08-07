
from PyQt5 import QtCore, QtGui, QtWidgets
from OTP_Generator import Ui_OTP_Gen
import sqlite3

class Ui_MainWindow(object):

    def openOTP_Gen(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_OTP_Gen()
        self.ui.setupUi(self.window)
        self.window.show()

    def loginTable(self):
        username=str(self.lineEdit.text())
        password=str(self.lineEdit_2.text())

        if (username == "abc" and password == "123"):
            self.openOTP_Gen()
        else:
            self.showMessageBox("Warning ","Please Enter Valid Username and Password !")

    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 399)
        MainWindow.setMinimumSize(QtCore.QSize(867, 399))
        MainWindow.setMaximumSize(QtCore.QSize(867, 399))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ###################### Labels ###################################
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 130, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 210, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        ####################### LineEdit ###############################
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 151, 271, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 233, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 40, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        ####################### PushButton #############################
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 310, 180, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginTable)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username :"))
        self.label_2.setText(_translate("MainWindow", "Password :"))
        self.pushButton.setText(_translate("MainWindow", "View User"))
        self.label_3.setText(_translate("MainWindow", "LOGIN FORM"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
