import threading 
from PyQt5 import QtCore, QtGui,  QtWidgets
from time import sleep
from PMS import Ui_MainWindow
from SplashScreen import Ui_Form
import os,sys

def splashScreen():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    def Close():
        Form.close()
    QtCore.QTimer.singleShot(5000, Close)
    sys.exit(app.exec_())

def PMS():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

STimer = threading.Timer(0, splashScreen)
PTimer = threading.Timer(5, PMS)
PTimer.start()
splashScreen()