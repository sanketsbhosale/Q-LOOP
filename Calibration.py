
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calibration(object):

    def CalDB(self):
        GaugeName=str(self.lineEdit.text())
        ReportDate=str(self.lineEdit_2.text())
        ReminderDate=str(self.lineEdit_7.text())

        if(len(GaugeName) == 0 and \
            len(ReportDate) == 0 and \
            len(ReminderDate) == 0):
            self.showCWMessageBox("Calibration","Please Enter Details!")
            print("Please Enter Details!")
            
        elif(len(GaugeName) == 0 and \
            len(ReportDate) == 0 ):
            self.showCWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(ReportDate) == 0 and \
            len(ReminderDate) == 0 ):
            self.showCWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(GaugeName) == 0 and \
            len(ReminderDate) == 0 ):
            self.showCWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(GaugeName) == 0):
            self.showCWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(ReportDate) == 0):
            self.showCWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(ReminderDate) == 0):
            self.showCWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        else:
            connection=sqlite3.connect("PYDB.db")
            c=connection.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS CalibrationTable(GAUGE_NAME TEXT PRIMARY KEY,REPORT_DATE TEXT NOT NULL,REMINDER_DATE TEXT NOT NULL)")
            c.execute("INSERT INTO CalibrationTable VALUES(?,?,?)",(GaugeName,ReportDate,ReminderDate))
            connection.commit()
            
            result=connection.execute("SELECT * FROM CalibrationTable WHERE GAUGE_NAME = ? AND REPORT_DATE = ?",(GaugeName,ReportDate))
            if (len(result.fetchone()) > 0):
                print("Details are added successfully!")
                self.showCMessageBox("Calibration","Details are Added successfully")
            c.close()

    def onClickCalDB(self):
        try:
            self.CalDB()
        except sqlite3.IntegrityError:
            self.showCWMessageBox("MSA","Details Exists !")

        ##################################################### CalDB Update ###################################

    def CalDBUpdate(self):

        GaugeName_1=str(self.lineEdit_3.text())
        GaugeName_2=str(self.lineEdit_4.text())
        ReportDate_1=str(self.lineEdit_5.text())
        ReminderDate_1=str(self.lineEdit_6.text())
        
        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        c.execute("UPDATE CalibrationTable SET REMINDER_DATE = ? , REPORT_DATE = ? , GAUGE_NAME = ? WHERE GAUGE_NAME = ?",(ReminderDate_1,ReportDate_1,GaugeName_2,GaugeName_1))
        c.execute("DELETE FROM CalibrationTable WHERE GAUGE_NAME = ?",(GaugeName_1,))
        connection.commit()
        result=connection.execute("SELECT * FROM CalibrationTable WHERE GAUGE_NAME = ?",(GaugeName_2,))

        if (len(result.fetchone()) > 0):
            print("Details are Updated successfully!")
            self.showCMessageBox("Calibration","Details are Updated successfully")
        c.close()

    def onClickCalDBUpdate(self):
        try:
            self.CalDBUpdate()
        except :
            print("Please re-enter Details")
            self.showCWMessageBox("Calibration","Please Re-Enter Details")

        ##################################################### CalDB Retrieval ########################################################

    def CalDBSearch(self):

        GaugeName=self.lineEdit_8.text()

        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        result=c.execute("SELECT * FROM CalibrationTable WHERE GAUGE_NAME = ?",(GaugeName,))
        connection.commit()

        try:
            for row in c.fetchall():
                ReportDate=self.lineEdit_9.setText(row[1])
                ReminderDate=self.lineEdit_10.setText(row[2])
                if row[0] != GaugeName:
                    self.showCWMessageBox("Calibration","Please Enter Valid Gauge Name")
        except:
            self.showCWMessageBox("Calibration","Please Enter Valid Gauge Name")

        c.close()
        connection.close()

        ##################################################### MsgBox #################################################################

    def showCMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showCWMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Calibration):
        Calibration.setObjectName("Calibration")
        Calibration.resize(1070, 572)
        Calibration.setMinimumSize(QtCore.QSize(1070, 572))
        Calibration.setMaximumSize(QtCore.QSize(1070, 572))
        Calibration.setStatusTip("")
        Calibration.setWhatsThis("")
        Calibration.setAccessibleName("")
        Calibration.setAccessibleDescription("")
        self.centralwidget = QtWidgets.QWidget(Calibration)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calibration.setWindowIcon(icon)

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

        ####################### NAME OF GAUGE ###################################
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

        ########################### DATE OF GAUGE ###############################

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

        ######################## DATE OF REMAINDER ##################################

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

        ########################### BUTTON ##########################################
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(650, 170, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClickCalDB)

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 240, 1011, 261))
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

        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 130, 631, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 170, 631, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 220, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.onClickCalDBUpdate)

        ############################# TAB 2 ##########################################

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(340, 30, 561, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 31, 101, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.CalDBSearch)

        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 90, 681, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(340, 150, 681, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(20, 150, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(0, -30, 1041, 541))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line.raise_()
        self.label_8.raise_()
        self.lineEdit_8.raise_()
        self.pushButton_3.raise_()
        self.lineEdit_9.raise_()
        self.label_9.raise_()
        self.lineEdit_10.raise_()
        self.label_10.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Calibration.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calibration)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Calibration)

    def retranslateUi(self, Calibration):
        _translate = QtCore.QCoreApplication.translate
        Calibration.setWindowTitle(_translate("Calibration", "Calibration"))
        self.groupBox.setTitle(_translate("Calibration", "Insert Calibration Details"))
        self.label.setText(_translate("Calibration", "Name of Gauge :"))
        self.label_2.setText(_translate("Calibration", "Date of gauge Calibration Report :"))
        self.label_7.setText(_translate("Calibration", "Date of Calibration Remainder :"))
        self.pushButton.setText(_translate("Calibration", "SUBMIT"))
        self.groupBox_2.setTitle(_translate("Calibration", "Edit Calibration Details"))
        self.label_3.setText(_translate("Calibration", "Name of Gauge :"))
        self.label_5.setText(_translate("Calibration", "New Date of gauge Calibration Report :"))
        self.label_4.setText(_translate("Calibration", "New Name of Gauge :"))
        self.label_6.setText(_translate("Calibration", "New Date of gauge Calibration Report :"))
        self.pushButton_2.setText(_translate("Calibration", "SUBMIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Calibration", "Insert and Edit Calibration Details"))
        self.label_8.setText(_translate("Calibration", "Name of Gauge :"))
        self.pushButton_3.setText(_translate("Calibration", "Search"))
        self.label_9.setText(_translate("Calibration", "Date of gauge Calibration Report :"))
        self.label_10.setText(_translate("Calibration", "Date of Calibration Remainder :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Calibration", "Show Calibration Details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calibration = QtWidgets.QMainWindow()
    ui = Ui_Calibration()
    ui.setupUi(Calibration)
    Calibration.show()
    sys.exit(app.exec_())

