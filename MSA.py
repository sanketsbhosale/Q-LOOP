
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MSA(object):

    def MSADB(self):
        MSAID=str(self.lineEdit.text())
        MSADate=str(self.lineEdit_2.text())
        MSAReminderDate=str(self.lineEdit_7.text())

        if(len(MSAID) == 0 and \
            len(MSADate) == 0 and \
            len(MSAReminderDate) == 0):
            self.showMSAWMessageBox("MSA","Please Enter Details!")
            print("Please Enter Details!")

        elif(len(MSAID) == 0 and \
            len(MSADate) == 0 ):
            self.showMSAWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MSAID) == 0 and \
            len(MSAReminderDate) == 0):
            self.showMSAWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MSADate) == 0 and \
            len(MSAReminderDate) == 0):
            self.showMSAWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MSAID) == 0 ):
            self.showMSAWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MSADate) == 0 ):
            self.showMSAWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")

        elif(len(MSAReminderDate) == 0):
            self.showMSAWMessageBox("Machine Capability","Please Enter all Details!")
            print("Please Enter Details!")
        else:
            connection=sqlite3.connect("PYDB.DB")
            connection.execute("CREATE TABLE IF NOT EXISTS MSATable(MSA_ID TEXT PRIMARY KEY,MSA_DATE TEXT,MSA_REMINDER_DATE TEXT)")
            connection.execute("INSERT INTO MSATable VALUES(?,?,?)",(MSAID,MSADate,MSAReminderDate))
            connection.commit()

            result=connection.execute("SELECT * FROM MSATable WHERE MSA_ID = ? AND MSA_DATE =?",(MSAID,MSADate))

            if (len (result.fetchone()) > 0):
                print("Details are added successfully!")
                self.showMSAMessageBox("MSA","Details are added successfully!")
                
            connection.close()

    def onClickMSA(self):
        try:
            self.MSADB()
        except sqlite3.IntegrityError:
            self.showMSAWMessageBox("MSA","Details Exists !")

    def MSADBUpdate(self):

        MSAID_1=str(self.lineEdit_3.text())
        MSADate_1=str(self.lineEdit_4.text())
        MSAReminderDate_1=str(self.lineEdit_6.text())
        
        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        c.execute("UPDATE MSATable SET MSA_REMINDER_DATE=?,MSA_DATE=? WHERE MSA_ID=?",(MSAReminderDate_1, MSADate_1, MSAID_1))
        connection.commit()
        result=connection.execute("SELECT * FROM MSATable WHERE MSA_ID = ?",(MSAID_1,))

        if (len(result.fetchone()) > 0):
            print("Details are Updated successfully!")
            self.showMSAMessageBox("MSA","Details are Updated successfully")

        c.close()

    def onClickMSAUpdate(self):
        try:
            self.MSADBUpdate()
        except :
            print("Please re-enter Details")
            self.showMSAWMessageBox("MSA","Please Re-Enter Details")

        ##################################################### CalDB Retrieval ########################################################

    def MSADBSearch(self):

        MSAID=self.lineEdit_8.text()

        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        result=c.execute("SELECT * FROM MSATable WHERE MSA_ID = ?",(MSAID,))
        connection.commit()

        try:
            for row in c.fetchall():
                ReportDate=self.lineEdit_9.setText(row[1])
                ReminderDate=self.lineEdit_10.setText(row[2])
                if row[0] != MSAID:
                    self.showCWMessageBox("MSA","Please Enter Valid Gauge Name")
        except:
            self.showCWMessageBox("MSA","Please Enter Valid Gauge Name")
        c.close()
        connection.close()

        ##################################################### MsgBox #################################################################
    def showMSAMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showMSAWMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, MSA):
        MSA.setObjectName("MSA")
        MSA.resize(1063, 540)
        MSA.setMinimumSize(QtCore.QSize(1063, 540))
        MSA.setMaximumSize(QtCore.QSize(1063, 540))
        MSA.setStatusTip("")
        MSA.setWhatsThis("")
        MSA.setAccessibleName("")
        MSA.setAccessibleDescription("")
        self.centralwidget = QtWidgets.QWidget(MSA)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MSA.setWindowIcon(icon)

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
        self.lineEdit.setGeometry(QtCore.QRect(350, 40, 631, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 80, 631, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 120, 631, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 291, 31))
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
        self.pushButton.clicked.connect(self.onClickMSA)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 240, 1011, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 50, 631, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 90, 631, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 130, 631, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 180, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.onClickMSAUpdate)
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
        self.pushButton_3.clicked.connect(self.MSADBSearch)
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(-3, -31, 1041, 521))
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
        MSA.setCentralWidget(self.centralwidget)

        self.retranslateUi(MSA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MSA)

    def retranslateUi(self, MSA):
        _translate = QtCore.QCoreApplication.translate
        MSA.setWindowTitle(_translate("MSA", "MSA"))
        self.groupBox.setTitle(_translate("MSA", "Insert MSA Details"))
        self.label.setText(_translate("MSA", "MSA ID :"))
        self.label_2.setText(_translate("MSA", "Date of MSA Report :"))
        self.label_7.setText(_translate("MSA", "Date of MSA Remainder :"))
        self.pushButton.setText(_translate("MSA", "SUBMIT"))
        self.groupBox_2.setTitle(_translate("MSA", "Edit MSA Details"))
        self.label_3.setText(_translate("MSA", "MSA ID :"))
        self.label_4.setText(_translate("MSA", "Date of MSA Report :"))
        self.label_6.setText(_translate("MSA", "Date of MSA Remainder:"))
        self.pushButton_2.setText(_translate("MSA", "SUBMIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MSA", "Insert and Edit MSA Details"))
        self.label_8.setText(_translate("MSA", "MSA ID :"))
        self.label_9.setText(_translate("MSA", "Date of gauge MSA Report :"))
        self.label_10.setText(_translate("MSA", "Date of MSA Remainder :"))
        self.pushButton_3.setText(_translate("MSA", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MSA", "Show MSA Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MSA = QtWidgets.QMainWindow()
    ui = Ui_MSA()
    ui.setupUi(MSA)
    MSA.show()
    sys.exit(app.exec_())

