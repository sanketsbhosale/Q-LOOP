
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from EnterCust import Ui_EnterCusto

class Ui_SearchCusto(object):

    def ShowEntCustMessageBox(self,title,message):  
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def ShowEntCustWMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    
    def companyDetailsDBSearch(self):
        
        BuyersCode=self.lineEdit.text()

        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        result=c.execute("SELECT * FROM CompanyDetTable WHERE BUYERS_CODE = ?",(BuyersCode,))
        print(result)
        self.tableWidget.setRowCount(0)

        for row in c.fetchall():
            if not c.fetchall:
                    self.ShowEntCustWMessageBox("Search Customer","Please Enter Valid Gauge Name 123")
            else:
                print(row)
                CompanyName=str(self.lineEdit_2.setText(row[1]))
                Address=str(self.lineEdit_3.setText(row[2]))
                CurrLiveComp=str(self.lineEdit_4.setText(str(row[3])))

                ProductName=str(self.lineEdit_6.setText(row[5]))
                ProductNo=str(self.lineEdit_5.setText(str(row[6])))
                MaterialGrade=str(self.lineEdit_7.setText(row[7]))
                MaterialSize=str(self.lineEdit_8.setText(str(row[8])))
                Price=str(self.lineEdit_9.setText(str(row[9])))
                CycleTime=str(self.lineEdit_10.setText(str(row[10])))

        connection.commit()
        c.close()
        connection.close

    def DeptDetailsDBAdd(self):
        BuyersCode=self.lineEdit.text()

        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
        self.tableWidget.setRowCount(0)

        result1=c.execute("SELECT DEPARTMENT, NAME , DESIGNATION , CONTACT_NO FROM DeptDetTable WHERE BUYERS_CODE1 = ?",(BuyersCode,))

        for row_number, row_data in enumerate(result1):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.tableWidget.setHorizontalHeaderLabels(('Department', 'Name', 'Designation','Contact No.'))

        connection.commit()
        c.close()
        connection.close

    def onClickCompDBSearch(self):
        try:
            #if 
            self.companyDetailsDBSearch()
            self.DeptDetailsDBAdd()
        except sqlite3.ProgrammingError:
            self.ShowEntCustWMessageBox("Customer Details","Please Enter Valid Buyers Code!")
        except sqlite3.OperationalError:
            self.ShowEntCustWMessageBox("Customer Details","Details not found!")
        except:
            self.ShowEntCustWMessageBox("Customer Details","There is ERROR in Searching Details!")


    def LoadData(self):
        ProductName=str(self.lineEdit_6.text())
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        name, _ = QtWidgets.QFileDialog.getSaveFileName(None,"Save File","","Image files (*.jpeg *.jpg);;All Files(*.*)", options=options)

        file=open(str(name) +'.jpeg','wb')
        
        connection=sqlite3.connect("PYDB.db")
        c=connection.cursor()
         
        c.execute("SELECT IMAGES FROM ProductDetailsTable_1 WHERE PRODUCT_NAME = ?", (ProductName,))
        result=c.fetchone()
        if not result:
            self.ShowEntCustMessageBox("Customer Details","ERROR in Downloading file !")
        else:
            file.write(result[0])
            self.ShowEntCustMessageBox("Customer Details","File saved successfully !")

        file.close()
        c.close()
        connection.close()

    def onClickLoadData(self):
        try:
            LoadData()
        except FileNotFoundError:
            self.ShowEntCustMessageBox("Search Customer Details","Please enter valid File name !")
        except sqlite3.IntegrityError:
            self.ShowPDIRWMessageBox("PDIR","File Exists !")
        except:
            self.ShowPDIRWMessageBox("PDIR","There is Problem in Uploading file")

    def setupUi(self, SearchCusto):
        SearchCusto.setObjectName("SearchCusto")
        SearchCusto.resize(1545, 727)
        SearchCusto.setMinimumSize(QtCore.QSize(1545, 727))
        SearchCusto.setMaximumSize(QtCore.QSize(1545, 727))
        self.centralwidget = QtWidgets.QWidget(SearchCusto)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchCusto.setWindowIcon(icon)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 32, 112, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(226, 32, 431, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(11, 58, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 75, 127, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(11, 169, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(11, 263, 187, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(11, 385, 741, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(120, 50))
        self.tableWidget.setRowCount(99)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(11, 357, 208, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(11, 909, 16, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(664, 30, 93, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClickCompDBSearch)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 10, 1531, 711))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(790, 452, 92, 21))
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(790, 394, 99, 21))
        self.label_11.setObjectName("label_11")

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(985, 220, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.LoadData)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(228, 80, 531, 81))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(790, 276, 120, 21))
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(790, 90, 97, 21))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(790, 220, 128, 21))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(790, 160, 115, 21))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(790, 335, 106, 21))
        self.label_10.setObjectName("label_10")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(780, 120, 751, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(790, 30, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(227, 170, 531, 81))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(228, 260, 531, 81))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(920, 81, 601, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(920, 160, 601, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(920, 270, 601, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(920, 330, 601, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(920, 388, 601, 41))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(920, 447, 601, 41))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_8.raise_()
        self.line_3.raise_()
        self.lineEdit_9.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.line.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.tableWidget.raise_()
        self.label_5.raise_()
        self.line_2.raise_()
        self.pushButton.raise_()
        self.label_12.raise_()
        self.label_11.raise_()
        self.toolButton.raise_()
        self.lineEdit_2.raise_()
        self.label_9.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.line_4.raise_()
        self.label_13.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_10.raise_()
        SearchCusto.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchCusto)
        QtCore.QMetaObject.connectSlotsByName(SearchCusto)

    def retranslateUi(self, SearchCusto):
        _translate = QtCore.QCoreApplication.translate
        SearchCusto.setWindowTitle(_translate("SearchCusto", "Search Customer Details"))
        self.label.setText(_translate("SearchCusto", "User\'s Code :"))
        self.label_2.setText(_translate("SearchCusto", "Company Name :"))
        self.label_3.setText(_translate("SearchCusto", "Address :"))
        self.label_4.setText(_translate("SearchCusto", "Current Live Complaints :"))
        self.label_5.setText(_translate("SearchCusto", "List Of Department Person :"))
        self.pushButton.setText(_translate("SearchCusto", "Search"))
        self.label_12.setText(_translate("SearchCusto", "Cycle Time :"))
        self.label_11.setText(_translate("SearchCusto", "Price (INR.) :"))
        self.toolButton.setText(_translate("SearchCusto", "DOWNLOAD"))
        self.label_9.setText(_translate("SearchCusto", "Material Grade :"))
        self.label_6.setText(_translate("SearchCusto", "Product No. :"))
        self.label_8.setText(_translate("SearchCusto", "Product Drawing "))
        self.label_7.setText(_translate("SearchCusto", "Product Name :"))
        self.label_10.setText(_translate("SearchCusto", "Material Size :"))
        self.label_13.setText(_translate("SearchCusto", "Product Details :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchCusto = QtWidgets.QMainWindow()
    ui = Ui_SearchCusto()
    ui.setupUi(SearchCusto)
    SearchCusto.show()
    sys.exit(app.exec_())

