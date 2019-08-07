# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(689, 197)
        About.setMinimumSize(QtCore.QSize(689, 197))
        About.setMaximumSize(QtCore.QSize(689, 197))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)

        self.textBrowser = QtWidgets.QTextBrowser(About)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 671, 141))
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton = QtWidgets.QPushButton(About)
        self.pushButton.setGeometry(QtCore.QRect(570, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(About.close)
        self.pushButton.clicked.connect(About.close)

        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(20, 10, 661, 131))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)
        
    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.pushButton.setText(_translate("About", "OK"))
        self.label.setText(_translate("About", "Q-LOOP 1.0.0\n""\n"
"Q-Loop is the system which supports the work environment where the set of activities\n"
" are there and to control and monitoring those activities, we need to getting support of\n"
" software technology."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

