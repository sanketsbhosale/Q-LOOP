from PyQt5 import QtCore, QtGui, QtWidgets
from threading import *
import sys
import time
import os
    

class Ui_Form(object):


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(901, 379)
        Form.setStyleSheet("QWidget{\n"
            "image: url(:/Images/NR-Hytech Banner31.jpg);\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgb(104, 104, 104);\n"
"border-color: rgb(255, 255, 255);"
"}\n"
"QLable{\n"
"}\n")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(372, 108, 151, 101))
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("Resource/logo2.bmp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(75, 320, 750, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("                                                             ...............   Loading Components    ...............")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


import SplashScreen_rc
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
