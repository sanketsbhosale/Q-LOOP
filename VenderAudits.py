
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VenderAudit(object):

    def VendAuditDB(self):
        VenderAuditID=str(self.lineEdit.text())
        VenderAuditDate=str(self.lineEdit_2.text())
        VenderAuditReminderDate=str(self.lineEdit_7.text())

        if(len(VenderAuditID) == 0 and \
            len(VenderAuditDate) == 0 and \
            len(VenderAuditReminderDate) == 0):
            self.showVAWMessageBox("Vender Audits","Please Enter Details!")
            print("Please Enter Details!")

        elif(len(VenderAuditID) == 0 and \
            len(VenderAuditDate) == 0 ):
            self.showVAWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(VenderAuditDate) == 0 and \
            len(VenderAuditReminderDate) == 0 ):
            self.showVAWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(VenderAuditID) == 0 and \
            len(VenderAuditReminderDate) == 0 ):
            self.showVAWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(VenderAuditID) == 0):
            self.showVAWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(VenderAuditDate) == 0):
            self.showVAWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        elif(len(VenderAuditReminderDate) == 0):
            self.showVAWMessageBox("Calibration","Please Enter all Details!")
            print("Please Enter all Details!")

        else:
            connection=sqlite3.connect("PYDB.db")
            connection.execute("CREATE TABLE IF NOT EXISTS Vender_AuditTable(VENDER_AUDIT_ID TEXT PRIMARY KEY,VENDER_AUDIT_DATE TEXT NOT NULL,VENDER_AUDIT_REMINDER_DATE NOT NULL)")
            connection.execute("INSERT INTO Vender_AuditTable VALUES(?,?,?)",(VenderAuditID,VenderAuditDate,VenderAuditReminderDate))
            connection.commit()
            result=connection.execute("SELECT * FROM Vender_AuditTable WHERE VENDER_AUDIT_ID = ? AND VENDER_AUDIT_DATE = ?",(VenderAuditID,VenderAuditDate))
            
            if (len(result.fetchone()) > 0):
                print("Details are added successfully!")
                self.showVAMessageBox("Vender Audits","Details are Added successfully")
                
            connection.close()

    def onClickVA(self):
        try:
            self.VendAuditDB()
        except sqlite3.IntegrityError:
            self.showVAWMessageBox("Vender Audits","Details Exists !")

    def VendAuditDBUpdate(self):

        VenderAuditID_1=str(self.lineEdit_3.text())
        VenderAuditDate_1=str(self.lineEdit_4.text())
        VenderAuditReminderDate_1=str(self.lineEdit_5.text())
        
        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        c.execute("UPDATE Vender_AuditTable SET VENDER_AUDIT_REMINDER_DATE=?,VENDER_AUDIT_DATE=? WHERE VENDER_AUDIT_ID=?",(VenderAuditReminderDate_1, VenderAuditDate_1,VenderAuditID_1))
        connection.commit()
        result=connection.execute("SELECT * FROM Vender_AuditTable WHERE VENDER_AUDIT_ID = ? AND VENDER_AUDIT_DATE = ?",(VenderAuditID_1,VenderAuditDate_1))

        if (len(result.fetchone()) > 0):
            print("Details are Updated successfully!")
            self.showVAMessageBox("Vender Audits","Details are Updated successfully")
        c.close()
        connection.close()

    def onClickVAUpdate(self):
        try:
            self.VendAuditDBUpdate()
        except:
            print("Please re-enter Details")
            self.showVAWMessageBox("Vender Audits","Please Re-Enter Details")

    def VADBSearch(self):

        VenderAuditID=self.lineEdit_8.text()

        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        result=c.execute("SELECT * FROM Vender_AuditTable WHERE VENDER_AUDIT_ID = ?",(VenderAuditID,))
        connection.commit()

        try:
            for row in c.fetchall():
                VenderAuditDate=self.lineEdit_9.setText(row[1])
                VenderAuditReminderDate=self.lineEdit_10.setText(row[2])
                if row[0] != VenderAuditID:
                    self.showVAWMessageBox("Calibration","Please Enter Valid Gauge Name")
        except:
            self.showVAWMessageBox("Calibration","Please Enter Valid Gauge Name")

        c.close()
        connection.close()

    def showVAMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showVAWMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, VenderAudit):
        VenderAudit.setObjectName("VenderAudit")
        VenderAudit.resize(1070, 528)
        VenderAudit.setMinimumSize(QtCore.QSize(1070, 528))
        VenderAudit.setMaximumSize(QtCore.QSize(1070, 528))
        VenderAudit.setStatusTip("")
        VenderAudit.setWhatsThis("")
        VenderAudit.setAccessibleName("")
        VenderAudit.setAccessibleDescription("")
        self.centralwidget = QtWidgets.QWidget(VenderAudit)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VenderAudit.setWindowIcon(icon)

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
        self.pushButton.clicked.connect(self.onClickVA)

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 240, 1011, 221))
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

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 180, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.onClickVAUpdate)

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
        self.pushButton_3.clicked.connect(self.VADBSearch)

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
        VenderAudit.setCentralWidget(self.centralwidget)

        self.retranslateUi(VenderAudit)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VenderAudit)

    def retranslateUi(self, VenderAudit):
        _translate = QtCore.QCoreApplication.translate
        VenderAudit.setWindowTitle(_translate("VenderAudit", "Vender Audits"))
        self.groupBox.setTitle(_translate("VenderAudit", "Insert Vender Audits Details"))
        self.label.setText(_translate("VenderAudit", "Vendor Audit ID :"))
        self.label_2.setText(_translate("VenderAudit", "Date of Vendor Audit :"))
        self.label_7.setText(_translate("VenderAudit", "Date of Vendor Audits Remainder :"))
        self.pushButton.setText(_translate("VenderAudit", "SUBMIT"))
        self.groupBox_2.setTitle(_translate("VenderAudit", "Edit Vender Audits Details"))
        self.label_3.setText(_translate("VenderAudit", "Vendor Audit ID :"))
        self.label_4.setText(_translate("VenderAudit", "Date of Vendor Audit :"))
        self.label_5.setText(_translate("VenderAudit", "Date of Vendor Audits Remainder :"))
        self.pushButton_2.setText(_translate("VenderAudit", "SUBMIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("VenderAudit", "Insert and Edit Vender Audits Details"))
        self.label_8.setText(_translate("VenderAudit", "Vender Audits ID :"))
        self.label_9.setText(_translate("VenderAudit", "Date of Vender Audits Report :"))
        self.label_10.setText(_translate("VenderAudit", "Date of Vender Audits Remainder :"))
        self.pushButton_3.setText(_translate("VenderAudit", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("VenderAudit", "Show Vender Audits Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VenderAudit = QtWidgets.QMainWindow()
    ui = Ui_VenderAudit()
    ui.setupUi(VenderAudit)
    VenderAudit.show()
    sys.exit(app.exec_())

