
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MachineCap(object):

    def MachCapDB(self):
        MachCapID=str(self.lineEdit.text())
        MachCapDate=str(self.lineEdit_2.text())
        MachCapReminderDate=str(self.lineEdit_7.text())

        if(len(MachCapID) == 0 and \
            len(MachCapDate) == 0 and \
            len(MachCapReminderDate) == 0):
            self.showMCWMessageBox("Machine Capability","Please Enter Details!")
            print("Please Enter Details!")

        elif(len(MachCapID) == 0 and \
            len(MachCapDate) == 0 ):
            self.showMCWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MachCapID) == 0 and \
            len(MachCapReminderDate) == 0):
            self.showMCWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MachCapDate) == 0 and \
            len(MachCapReminderDate) == 0):
            self.showMCWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MachCapID) == 0 ):
            self.showMCWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MachCapDate) == 0 ):
            self.showMCWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MachCapReminderDate) == 0):
            self.showMCWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        else:
            connection=sqlite3.connect("PYDB.db")
            connection.execute("CREATE TABLE IF NOT EXISTS Machine_capabilityTable(MACHINE_CAPABILITY_ID PRIMARY KEY,MACHINE_CAPABILITY_DATE TEXT NOT NULL,MACHINE_CAPABILITY_REMINDER_DATE TEXT NOT NULL)")
            connection.execute("INSERT INTO Machine_capabilityTable VALUES(?,?,?)",(MachCapID,MachCapDate,MachCapReminderDate))
            connection.commit()
            result=connection.execute("SELECT * FROM Machine_capabilityTable WHERE MACHINE_CAPABILITY_ID = ? AND MACHINE_CAPABILITY_DATE =?",(MachCapID,MachCapDate))
            
            if (len(result.fetchone()) > 0):
                print("Details are added successfully!")
                self.showMCMessageBox("Machine Capability","Details are Added successfully!")

    def onClickMCDB(self):
        try:
            self.MachCapDB()
        except sqlite3.IntegrityError:
            self.showMCWMessageBox("Machine Capability","Details Exists !")
                    
    def MachCapDBUpdate(self):

        MachCapID_1=str(self.lineEdit_3.text())
        MachCapDate_1=str(self.lineEdit_4.text())
        MachCapReminderDate_1=str(self.lineEdit_6.text())
        
        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        c.execute("UPDATE Machine_capabilityTable SET MACHINE_CAPABILITY_REMINDER_DATE=?,MACHINE_CAPABILITY_DATE=? WHERE MACHINE_CAPABILITY_ID=?",(MachCapReminderDate_1, MachCapDate_1,MachCapID_1))
        connection.commit()
        result=connection.execute("SELECT * FROM Machine_capabilityTable WHERE MACHINE_CAPABILITY_ID = ? AND MACHINE_CAPABILITY_DATE = ?",(MachCapID_1,MachCapDate_1))

        if (len(result.fetchone()) > 0):
            print("Details are Updated successfully!")
            self.showMCMessageBox("Machine Capability","Details are Updated successfully")

    def onClickMCDBUpdate(self):
        try:
            self.MachCapDBUpdate()
        except :
            print("Please re-enter Details")
            self.showMCMessageBox("Mahcine Capability","Please Re-Enter Details")

    def MCDBSearch(self):

        MachCapID=self.lineEdit_8.text()

        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        result=c.execute("SELECT * FROM Machine_capabilityTable WHERE MACHINE_CAPABILITY_ID = ?",(MachCapID,))
        connection.commit()

        try:
            for row in c.fetchall():
                MachCapDate=self.lineEdit_9.setText(row[1])
                MachCapReminderDate=self.lineEdit_10.setText(row[2])
                if (MachCapID != row[0]):
                    self.showMCMessageBox("Machine Capability","Please Enter Valid Gauge Name")
        except:
            self.showMCWMessageBox("Machine Capability","Please Enter Valid Gauge Name")

        c.close()
        connection.close()

    def showMCMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_() 

    def showMCWMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, MachineCap):
        MachineCap.setObjectName("MachineCap")
        MachineCap.resize(1068, 529)
        MachineCap.setMinimumSize(QtCore.QSize(1068, 529))
        MachineCap.setMaximumSize(QtCore.QSize(1068, 529))
        MachineCap.setStatusTip("")
        MachineCap.setWhatsThis("")
        MachineCap.setAccessibleName("")
        MachineCap.setAccessibleDescription("")
        self.centralwidget = QtWidgets.QWidget(MachineCap)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MachineCap.setWindowIcon(icon)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1011, 221))
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(400, 40, 581, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 80, 581, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(400, 120, 581, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(650, 170, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClickMCDB)

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 240, 1011, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(400, 50, 581, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(400, 90, 581, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(400, 130, 581, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 180, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.onClickMCDBUpdate)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(340, 29, 561, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 89, 681, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 29, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 89, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(20, 149, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(340, 149, 681, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 30, 101, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.MCDBSearch)

        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(0, -30, 1041, 501))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_9.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.lineEdit_10.raise_()
        self.pushButton_3.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MachineCap.setCentralWidget(self.centralwidget)

        self.retranslateUi(MachineCap)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MachineCap)

    def retranslateUi(self, MachineCap):
        _translate = QtCore.QCoreApplication.translate
        MachineCap.setWindowTitle(_translate("MachineCap", "Machine Capability"))
        self.groupBox.setTitle(_translate("MachineCap", "Insert Machine Capability Details"))
        self.label.setText(_translate("MachineCap", "Machine Capability ID :"))
        self.label_2.setText(_translate("MachineCap", "Date of Machine Capability :"))
        self.label_7.setText(_translate("MachineCap", "Date of Machine Capability Remainder :"))
        self.pushButton.setText(_translate("MachineCap", "SUBMIT"))
        self.groupBox_2.setTitle(_translate("MachineCap", "Edit Machine Capability Details"))
        self.label_3.setText(_translate("MachineCap", "Machine Capability ID :"))
        self.label_4.setText(_translate("MachineCap", "Date of Machine Capability :"))
        self.label_6.setText(_translate("MachineCap", "Date of Machine Capability Remainder :"))
        self.pushButton_2.setText(_translate("MachineCap", "SUBMIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MachineCap", "Insert and Edit Machine Capability Details"))
        self.label_8.setText(_translate("MachineCap", "Machine Capability ID:"))
        self.label_9.setText(_translate("MachineCap", "Date of Machine Capability Report :"))
        self.label_10.setText(_translate("MachineCap", "Date of Machine Capability Remainder :"))
        self.pushButton_3.setText(_translate("MachineCap", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MachineCap", "Show Machine Capabilty Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MachineCap = QtWidgets.QMainWindow()
    ui = Ui_MachineCap()
    ui.setupUi(MachineCap)
    MachineCap.show()
    sys.exit(app.exec_())

