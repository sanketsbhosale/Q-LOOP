
import requests
import bs4
import html.parser
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_1(object):
    def WebScrapper(self):

        try:
            Website=str(self.lineEdit.text())

            res = requests.get(Website)
            soup = bs4.BeautifulSoup(res.text ,'html.parser')
            Contents=soup.select('div')
            self.textEdit.setText(str(Contents))
        except requests.exceptions.MissingSchema:
            self.showCWMessageBox("Web Scrapper Tool","Please Enter Website Link")
        except:
            self.showCWMessageBox("Web Scrapper Tool","Please Make Sure that, you are connected to internet !")

    def WebScrapper_2(self):

        try:
            Website=str(self.lineEdit.text())

            res = requests.get(Website)
            soup = bs4.BeautifulSoup(res.text ,'html.parser')
            for i in soup.find_all('a',href=True):
                a=i['href']
            self.textEdit_2.setText(str(a))
        except requests.exceptions.MissingSchema:
            self.showCWMessageBox("Web Scrapper Tool","Please Enter Website Link")
        except:
            self.showCWMessageBox("Web Scrapper Tool","Please Make Sure that, you are connected to internet !")

    def showCWMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1302, 837)
        MainWindow.setMinimumSize(QtCore.QSize(1289, 843))
        MainWindow.setMaximumSize(QtCore.QSize(1289, 843))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 30, 941, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(370, 117, 161, 41))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.WebScrapper)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 167, 1181, 271))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 127, 291, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 514, 1181, 281))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 464, 281, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(370, 455, 161, 41))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.WebScrapper_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Scrapper Tool (BETA)"))
        self.toolButton.setText(_translate("MainWindow", "Get the Details !!!"))
        self.label.setText(_translate("MainWindow", "Contents :"))
        self.label_2.setText(_translate("MainWindow", "Links :"))
        self.label_3.setText(_translate("MainWindow", "Put your Link here ! >>>"))
        self.toolButton_2.setText(_translate("MainWindow", "Get the Details !!!"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())