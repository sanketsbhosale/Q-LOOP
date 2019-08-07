
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

class Ui_PDIR(object):

    def ShowPDIRWMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def ShowPDIRMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    ################################## PDIR ####################################
    def PDIRUpload(self,PDIRName):
    
        PDIRName=str(self.lineEdit.text())
        if len(PDIRName) == 0:
            self.ShowPDIRWMessageBox("PDIR","Please Enter PDIR Name")
        else:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            name, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',"","Microsoft EXCEL files (*.xlsx *.xls);;All Files(*.*)",  options=options)
            file=open(PDIRName +'.xlsx','rb')

            connection=sqlite3.connect("PYDB.db")
            c=connection.cursor()

            sql = "CREATE TABLE IF NOT EXISTS PDIRTable(PDIR_NAME TEXT,IMAGES BLOB)"
            sql1= "INSERT INTO PDIRTable VALUES(?,?)"

            c.execute(sql)
            c.execute(sql1, (PDIRName,sqlite3.Binary(file.read())) )

            connection.commit()

            result=c.execute("SELECT * FROM PDIRTable WHERE PDIR_Name = ?",(PDIRName,))
        
            if (len(result.fetchone()) > 0):
                self.ShowPDIRMessageBox("PDIR","File is uploaded successfully !")

            c.close()
            connection.close()

    def onClickPDIRU(self,PDIRName):
        try:
            self.PDIRUpload(PDIRName)
        except FileNotFoundError:
            self.ShowPDIRMessageBox("PDIR","Please enter valid File name !")
        except sqlite3.IntegrityError:
            self.ShowPDIRWMessageBox("PDIR","File Exists !")
        except:
            self.ShowPDIRWMessageBox("PDIR","There is Problem in Uploading file")

    def PDIRDownload(self):

        PDIRName2=str(self.lineEdit_2.text())
        if len(PDIRName2) == 0:
            self.ShowPDIRWMessageBox("PDIR","Please Enter PDIR Name")
        else:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            name, _ = QtWidgets.QFileDialog.getSaveFileName(None,"Save File","","Microsoft EXCEL files (*.xlsx *.xls);;All Files(*.*)", options=options)

            file=open(str(name) +'.xlsx','wb')
        
            connection=sqlite3.connect("PYDB.db")
            c=connection.cursor()
         
            c.execute("SELECT IMAGES FROM PDIRTable WHERE PDIR_NAME = ?", (PDIRName2,))
            result=c.fetchone()

            if not result:
                self.ShowPDIRMessageBox("PDIR","ERROR - PDIR Name does not match with '" + PDIRName2 + "'")
            else:
                file.write(result[0])
                self.ShowPDIRMessageBox("PDIR","File saved successfully !")
          
            connection.commit()
            c.close()
            connection.close()

    def onClickPDIRD(self):
        try:
            self.PDIRDownload()
        except FileNotFoundError:
            self.ShowPDIRMessageBox("PDIR","Please enter valid File name !")
        except sqlite3.IntegrityError:
            self.ShowPDIRWMessageBox("PDIR","File Exists !")
        except:
            self.ShowPDIRWMessageBox("PDIR","There is Problem in Downloading file")

     ##################################################### Drawing #########################################################

    def DrawingUpload(self,DrawingName):

        DrawingName=str(self.lineEdit_3.text())
        if len(DrawingName) == 0:
            self.ShowPDIRWMessageBox("Drawing","Please Enter Drawing Name")
        else:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            name, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',"","Image files (*.JPEG *.JPG);;All Files(*.*)",  options=options)
            file=open(DrawingName +'.jpeg','rb')

            connection=sqlite3.connect("PYDB.db")
            c=connection.cursor()

            c.execute("CREATE TABLE IF NOT EXISTS DrawingTable(DRAWING_NAME TEXT,IMAGES BLOB)")
            c.execute("INSERT INTO DrawingTable VALUES(?,?)", (DrawingName,sqlite3.Binary(file.read())) )

            connection.commit()

            result=c.execute("SELECT * FROM DrawingTable WHERE DRAWING_NAME = ?",(DrawingName,))
        
            if (len(result.fetchone()) > 0):
                self.ShowPDIRMessageBox("Drawing ","File is uploaded successfully !")

            c.close()
            connection.close()

    def onClickDraw(self,DrawingName):
        try:
            self.DrawingUpload(DrawingName)
        except FileNotFoundError:
            self.ShowPDIRMessageBox("Drawing","Please enter valid File name !")
        except sqlite3.IntegrityError:
            self.ShowPDIRWMessageBox("Drawing","File Exists !")
        except:
            self.ShowPDIRWMessageBox("Drawing","There is Problem in Uploading file")

    def DrawingDownload(self):

        DrawingName2=str(self.lineEdit_4.text())
        if len(DrawingName2) == 0:
            self.ShowPDIRWMessageBox("Drawing","Please Enter Drawing Name")
        else:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            name, _ = QtWidgets.QFileDialog.getSaveFileName(None,"Save File","","Image files (*.JPEG *.JPG);;All Files(*.*)", options=options)

            file=open(str(name) +'.jpeg','wb')
            connection=sqlite3.connect("PYDB.db")
            c=connection.cursor()

            c.execute("SELECT IMAGES FROM DrawingTable WHERE DRAWING_NAME = ?",(DrawingName2,))
            result=c.fetchone()

            if not result:
                self.ShowPDIRMessageBox("Drawing","ERROR- Drawing Name does not match with '" + DrawingName2 + "'" )
            else:
                file.write(result[0])
                self.ShowPDIRMessageBox("Drawing","File saved successfully !")

            connection.commit()
            c.close()
            connection.close()

    def onClickDrawD(self):
        try:
            self.DrawingDownload()
        except FileNotFoundError:
            self.ShowPDIRMessageBox("Drawing","Please enter valid File name !")
        except sqlite3.IntegrityError:
            self.ShowPDIRWMessageBox("Drawing","File Exists !")
        except:
            self.ShowPDIRWMessageBox("Drawing","There is Problem in Downloading file")

    ############################################### Chemical Report #########################################################
    def ChemicalReportUpload(self,ChemicalName):

        ChemicalName = str(self.lineEdit_5.text())
        if len(ChemicalName) == 0:
            self.ShowPDIRWMessageBox("Chemical Report","Please Enter Chemical Report Name")
        else:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            name, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',"","Portable Document Files (*.PDF);;All Files(*.*)",  options=options)
            file=open(ChemicalName +'.PDF','rb')
        
            connection=sqlite3.connect("PYDB.db")
            c=connection.cursor()
        
            c.execute("CREATE TABLE IF NOT EXISTS ChemRepoTable(CHEMICAL_NAME TEXT,IMAGES BLOB)")
            c.execute("INSERT INTO ChemRepoTable VALUES(?,?)", (ChemicalName,sqlite3.Binary(file.read())) )

            connection.commit()

            result=connection.execute("SELECT * FROM ChemRepoTable WHERE CHEMICAL_NAME = ?",(ChemicalName,))
            
            if (len(result.fetchone()) > 0):
                self.ShowPDIRMessageBox("Chemical Report","File is uploaded successfully !")

            c.close()
            connection.close()

    def onClickChem(self,ChemicalName):
        try:
            self.ChemicalReportUpload(ChemicalName)
        except FileNotFoundError:
            self.ShowPDIRMessageBox("Chemical Report","Please enter valid File name !")
        except sqlite3.IntegrityError:
            self.ShowPDIRWMessageBox("Chemical Report","File Exists !")
        except:
            self.ShowPDIRWMessageBox("Chemical Report","There is Problem in Uploading file")

    def ChemicalReportDownload(self):

        ChemicalName2 = str(self.lineEdit_6.text())

        if len(ChemicalName2) == 0:
            self.ShowPDIRWMessageBox("Chemical Report","Please Enter Chemical Report Name")
        else:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            name, _ = QtWidgets.QFileDialog.getSaveFileName(None,"Save File","","Portable Document Files (*.PDF);;All Files(*.*)", options=options)

            file=open(str(name) +'.pdf','wb')
            connection=sqlite3.connect("PYDB.db")
            c=connection.cursor()

            c.execute("SELECT IMAGES FROM ChemRepoTable WHERE CHEMICAL_NAME = ?",(ChemicalName2,))
            result=c.fetchone()

            if not result:
                self.ShowPDIRMessageBox("Chemical Report","ERROR- Chemical Report Name does not match with '" +  ChemicalName2 + "'")
            else:
                file.write(result[0])
                self.ShowPDIRMessageBox("Chemical Report","File saved successfully !")

            connection.commit()
            c.close()
            connection.close()
     
    def onClickChemD(self):
            try:
                self.ChemicalReportDownload()
            except FileNotFoundError:
                 self.ShowPDIRMessageBox("Drawing","Please enter valid File name !")
            except sqlite3.IntegrityError:
                 self.ShowPDIRWMessageBox("Drawing","File Exists !")
            except:
                 self.ShowPDIRWMessageBox("Drawing","There is Problem in Downloading file")

    ############################################################ Heat Treatment ##############################################
    def HeatTreatmentUpload(self,HeatTreatmentName):

        HeatTreatmentName = str(self.lineEdit_8.text())
        if len(HeatTreatmentName) == 0:
            self.ShowPDIRWMessageBox("Heat Treatment","Please Enter Heat Treatment Name")
        else:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            name, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',"","Portable Document Files (*.PDF);;All Files(*.*)",  options=options)
            file=open(HeatTreatmentName +".pdf",'rb')

            connection=sqlite3.connect("PYDB.db")
            c=connection.cursor()

            c.execute("CREATE TABLE IF NOT EXISTS HeatTreatmentTable(HEAT_TREATMENT_NAME TEXT,IMAGES BLOB)")
            c.execute("INSERT INTO HeatTreatmentTable VALUES(?,?)", (HeatTreatmentName,sqlite3.Binary(file.read())) )

            connection.commit()

            result=connection.execute("SELECT * FROM HeatTreatmentTable WHERE HEAT_TREATMENT_NAME = ?",(HeatTreatmentName,))
             
            if (len(result.fetchone()) > 0):
                self.ShowPDIRMessageBox("Heat Treatment","File is uploaded successfully")

            c.close()
            connection.close()

    def onClickHeat(self,HeatTreatmentName):
        try:
            self.HeatTreatmentUpload(HeatTreatmentName)
        except FileNotFoundError:
            self.ShowPDIRMessageBox("Heat Treatment","Please enter valid File name !")
        except sqlite3.IntegrityError:
            self.ShowPDIRWMessageBox("Heat Treatment","File Exists !")
        except:
            self.ShowPDIRWMessageBox("Heat Treatment","There is Problem in Uploading file")

    def HeatTreatmentDownload(self):

        HeatTreatmentName2 = str(self.lineEdit_7.text())

        if len(HeatTreatmentName2) == 0:
            self.ShowPDIRWMessageBox("Heat Treatment","Please Enter Heat Treatment Name")
        else:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            name, _ = QtWidgets.QFileDialog.getSaveFileName(None,"Save File","","Portable Document Files (*.PDF);;All Files(*.*)", options=options)

            file=open(str(name) +'.pdf','wb')

            connection=sqlite3.connect("PYDB.db")
            c=connection.cursor()

            c.execute("SELECT IMAGES FROM HeatTreatmentTable WHERE HEAT_TREATMENT_NAME = ?",(HeatTreatmentName2,))
            result=c.fetchone()

            if not result:
                self.ShowPDIRMessageBox("Heat Treatment","ERROR- Heat Treatment Name does not match with '" + HeatTreatmentName2 + "'")
            else:
                file.write(result[0])
                self.ShowPDIRMessageBox("Heat Treatment","File saved successfully !")

            connection.commit()
            c.close()
            connection.close()

    def onClickHeatD(self):
        try:
            self.HeatTreatmentDownload()
        except FileNotFoundError:
            self.ShowPDIRMessageBox("Heat Treatment","Please enter valid File name !")
        except sqlite3.IntegrityError:
            self.ShowPDIRWMessageBox("Heat Treatment","File Exists !")
        except:
            self.ShowPDIRWMessageBox("Heat Treatment","There is Problem in Downloading file")

    def setupUi(self, PDIR):

        PDIR.setObjectName("PDIR")
        PDIR.resize(798, 659)
        PDIR.setMinimumSize(QtCore.QSize(798, 659))
        PDIR.setMaximumSize(QtCore.QSize(798, 659))
        PDIR.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        PDIR.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(PDIR)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-3, 0, 801, 611))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 791, 631))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PDIR.setWindowIcon(icon)

        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 361, 281))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(170, 90, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClickPDIRU)

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 200, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.onClickPDIRD)

        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(170, 40, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 150, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(30, 150, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 10, 361, 281))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 90, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.onClickDraw)

        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 200, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.onClickDrawD)

        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(30, 40, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 40, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 150, 131, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(30, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 320, 361, 281))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 100, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.onClickChem)

        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 210, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.onClickChemD)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 50, 121, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 160, 121, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 160, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(420, 320, 361, 281))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 100, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.onClickHeat)

        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(221, 210, 121, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.onClickHeatD)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(220, 160, 131, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(10, 160, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(220, 50, 131, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(10, 50, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        PDIR.setCentralWidget(self.centralwidget)

        self.retranslateUi(PDIR)
        QtCore.QMetaObject.connectSlotsByName(PDIR)

    def retranslateUi(self, PDIR):
        _translate = QtCore.QCoreApplication.translate
        PDIR.setWindowTitle(_translate("PDIR", "PDIR"))

        self.groupBox.setTitle(_translate("PDIR", "PDIR"))
        self.pushButton.setText(_translate("PDIR", "UPLOAD"))
        self.label.setText(_translate("PDIR", "Upload PDIR :"))
        self.label_5.setText(_translate("PDIR", "Download PDIR :"))
        self.pushButton_5.setText(_translate("PDIR", "DOWNLOAD"))
        self.label_10.setText(_translate("PDIR", "PDIR Name :"))
        self.label_11.setText(_translate("PDIR", "PDIR Name :"))

        self.groupBox_2.setTitle(_translate("PDIR", "Drawing"))
        self.pushButton_2.setText(_translate("PDIR", "UPLOAD"))
        self.label_2.setText(_translate("PDIR", "Upload Drawing :"))
        self.label_6.setText(_translate("PDIR", "Download Drawing :"))
        self.pushButton_6.setText(_translate("PDIR", "DOWNLOAD"))
        self.label_9.setText(_translate("PDIR", "Drawing Name :"))
        self.label_12.setText(_translate("PDIR", "Drawing Name :"))

        self.groupBox_3.setTitle(_translate("PDIR", "Chemical Report"))
        self.pushButton_3.setText(_translate("PDIR", "UPLOAD"))
        self.label_3.setText(_translate("PDIR", "Upload Chemical Report :"))
        self.label_7.setText(_translate("PDIR", "Download Chemical Report :"))
        self.pushButton_7.setText(_translate("PDIR", "DOWNLOAD"))
        self.label_13.setText(_translate("PDIR", "Chemical Report Name :"))
        self.label_14.setText(_translate("PDIR", "Chemical Report Name :"))

        self.groupBox_4.setTitle(_translate("PDIR", "Heat Treatment"))
        self.pushButton_4.setText(_translate("PDIR", "UPLOAD"))
        self.label_4.setText(_translate("PDIR", "Upload Heat Treatment :"))
        self.label_8.setText(_translate("PDIR", "Download Heat Treatment :"))
        self.pushButton_8.setText(_translate("PDIR", "DOWNLOAD"))
        self.label_15.setText(_translate("PDIR", "Heat Treatment Name :"))
        self.label_16.setText(_translate("PDIR", "Heat Treatment Name :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PDIR = QtWidgets.QMainWindow()
    ui = Ui_PDIR()
    ui.setupUi(PDIR)
    PDIR.show()
    sys.exit(app.exec_())

