
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExceltoPDF(object):

    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def exceltoPDF(self):

        nameE=str(self.lineEdit.text())
        nameP=str(self.lineEdit_2.text())

        if (len(nameE) > 0 and len(nameP) > 0):
            from win32com import client
            xlApp = client.Dispatch("Excel.Application")
            books = xlApp.Workbooks.Open(nameE)
            ws = books.Worksheets[0]
            ws.Visible = 1
            ws.ExportAsFixedFormat(0, nameP)
        else:
            self.showMessageBox("Excel to PDF Converter","Please Enter Valid Path !!!")

    def onClickETP(self):
        try:
            self.exceltoPDF()
        except:
            self.showMessageBox("Excel to PDF Converter","Please Enter Valid Path")

    def setupUi(self, ExceltoPDF):
        ExceltoPDF.setObjectName("ExceltoPDF")
        ExceltoPDF.resize(395, 225)
        ExceltoPDF.setMinimumSize(QtCore.QSize(395, 225))
        ExceltoPDF.setMaximumSize(QtCore.QSize(395, 225))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExceltoPDF.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(ExceltoPDF)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 71, 31))
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.exceltoPDF)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 41, 271, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 100, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        ExceltoPDF.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExceltoPDF)
        QtCore.QMetaObject.connectSlotsByName(ExceltoPDF)

    def retranslateUi(self, ExceltoPDF):
        _translate = QtCore.QCoreApplication.translate
        ExceltoPDF.setWindowTitle(_translate("ExceltoPDF", "EXCEL to PDF Converter"))
        self.label.setText(_translate("ExceltoPDF", "EXCEL file"))
        self.label_2.setText(_translate("ExceltoPDF", "PDF file"))
        self.pushButton.setText(_translate("ExceltoPDF", "Convert"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExceltoPDF = QtWidgets.QMainWindow()
    ui = Ui_ExceltoPDF()
    ui.setupUi(ExceltoPDF)
    ExceltoPDF.show()
    sys.exit(app.exec_())
