import MainPage_rc
import Rersources_rc
from PyQt5 import QtCore, QtGui,  QtWidgets
from EnterCust import Ui_EnterCusto
from searchCust import Ui_SearchCusto
from PDIR import Ui_PDIR
from InhouseNonConformance import Ui_InNonConf
from CustomerNonConformance import Ui_CustNonConf
from PPC import Ui_PPCalc
from MachineCapability import Ui_MachineCap
from VenderAudits import Ui_VenderAudit
from Calibration import Ui_Calibration
from SPC import Ui_SPC
from MSA import Ui_MSA
from About import Ui_About
from WebScraping import Ui_MainWindow_1
from ExceltoPDF import Ui_ExceltoPDF
from SplashScreen import Ui_Form
from threading import *
import time

class Ui_MainWindow(object):

    def openEnterCust(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_EnterCusto()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSearchCust(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_SearchCusto()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPDIR(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_PDIR()
        self.ui.setupUi(self.window)
        self.window.show()

    def openInhouseNonConf(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_InNonConf()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCustNonConf(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_CustNonConf()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPPCalc(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_PPCalc()
        self.ui.setupUi(self.window)
        self.window.show()

    def openMachineCapability(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MachineCap()
        self.ui.setupUi(self.window)
        self.window.show()

    def openVenderAudits(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_VenderAudit()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCalibration(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Calibration()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSPC(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_SPC()
        self.ui.setupUi(self.window)
        self.window.show()

    def openMSA(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MSA()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAbout(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_About()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWebScrapperTool(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow_1()
        self.ui.setupUi(self.window)
        self.window.show()

    def openExcelToPDF(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_ExceltoPDF()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        start_time=time.time()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 839)
        MainWindow.showMaximized()
                
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(674, 132))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/logo2.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setStyleSheet("image: url(:/Main/NR-Hytech Banner.png);\n"
"border-image: url(:/Main/NR-Hytech Banner1.jpg);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 3)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("image: url(:/Main/products.jpg);\n"
"border-image: url(:/Main/products1.jpg);")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("image: url(:/Main/Screenshot 2019-02-09 16.51.25.png);\n"
"border-image: url(:/Main/Screenshot 2019-02-09 16.51.253.jpg);")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setStyleSheet("image: url(:/Main/broucher.jpg);\n"
"border-image: url(:/Main/broucher1.jpg);\n"
"border-image: url(:/Main/broucher1.jpg);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 2, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 26))
        self.menubar.setObjectName("menubar")

        self.menuCustomer_Details = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.menuCustomer_Details.setFont(font)
        self.menuCustomer_Details.setObjectName("menuCustomer_Details")

        self.menuQMS = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.menuQMS.setFont(font)
        self.menuQMS.setObjectName("menuQMS")

        self.menuNon_Conformance = QtWidgets.QMenu(self.menuQMS)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.menuNon_Conformance.setFont(font)
        self.menuNon_Conformance.setObjectName("menuNon_Conformance")

        self.menuPart_Production_Calculator = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.menuPart_Production_Calculator.setFont(font)
        self.menuPart_Production_Calculator.setObjectName("menuPart_Production_Calculator")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuReiceive_Material = QtWidgets.QMenu(self.menubar)
        self.menuReiceive_Material.setObjectName("menuReiceive_Material")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setStyleSheet("")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        ###################################### EVENT Handlers ####################################

        self.actionEnter_Customer_Details = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.actionEnter_Customer_Details.setFont(font)
        self.actionEnter_Customer_Details.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionEnter_Customer_Details.setObjectName("actionEnter_Customer_Details")
        self.actionEnter_Customer_Details.triggered.connect(self.openEnterCust)

        self.actionSearch_Customer_Details = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.actionSearch_Customer_Details.setFont(font)
        self.actionSearch_Customer_Details.setObjectName("actionSearch_Customer_Details")
        self.actionSearch_Customer_Details.triggered.connect(self.openSearchCust)

        self.actionPDIR = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/PDIR.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPDIR.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.actionPDIR.setFont(font)
        self.actionPDIR.setObjectName("actionPDIR")
        self.actionPDIR.triggered.connect(self.openPDIR)

        self.actionCustomer = QtWidgets.QAction(MainWindow)
        self.actionCustomer.setObjectName("actionCustomer")
        self.actionCustomer.triggered.connect(self.openCustNonConf)

        self.actionInhouse = QtWidgets.QAction(MainWindow)
        self.actionInhouse.setObjectName("actionInhouse")
        self.actionInhouse.triggered.connect(self.openInhouseNonConf)

        self.actionCalibration = QtWidgets.QAction(MainWindow)
        self.actionCalibration.setObjectName("actionCalibration")
        self.actionCalibration.triggered.connect(self.openCalibration)

        self.actionMachine_Capability = QtWidgets.QAction(MainWindow)
        self.actionMachine_Capability.setObjectName("actionMachine_Capability")
        self.actionMachine_Capability.triggered.connect(self.openMachineCapability)

        self.actionSPC = QtWidgets.QAction(MainWindow)
        self.actionSPC.setObjectName("actionSPC")
        self.actionSPC.triggered.connect(self.openSPC)

        self.actionMSA = QtWidgets.QAction(MainWindow)
        self.actionMSA.setObjectName("actionMSA")
        self.actionMSA.triggered.connect(self.openMSA)

        self.actionVender_Audits = QtWidgets.QAction(MainWindow)
        self.actionVender_Audits.setObjectName("actionVender_Audits")
        self.actionVender_Audits.triggered.connect(self.openVenderAudits)

        self.actionPPC = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/PPC.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPPC.setIcon(icon1)
        self.actionPPC.setObjectName("actionPPC")
        self.actionPPC.triggered.connect(self.openPPCalc)

        self.WebScrapingtool = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Web Scrapper (2).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.WebScrapingtool.setIcon(icon2)
        self.WebScrapingtool.setObjectName("WebScrapingtool")
        self.WebScrapingtool.triggered.connect(self.openWebScrapperTool)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.openAbout)

        self.actionEXCELToPDF = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/microsoft_excel_logo_primary_resized.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEXCELToPDF.setIcon(icon3)
        self.actionEXCELToPDF.setObjectName("actionEXCELToPDF")
        self.actionEXCELToPDF.triggered.connect(self.openExcelToPDF)

        self.menuCustomer_Details.addAction(self.actionEnter_Customer_Details)
        self.menuCustomer_Details.addAction(self.actionSearch_Customer_Details)
        self.menuNon_Conformance.addAction(self.actionCustomer)
        self.menuNon_Conformance.addAction(self.actionInhouse)
        self.menuQMS.addAction(self.actionPDIR)
        self.menuQMS.addAction(self.menuNon_Conformance.menuAction())
        self.menuPart_Production_Calculator.addAction(self.actionPPC)
        self.menuAbout.addAction(self.actionAbout)
        self.menuReiceive_Material.addAction(self.actionCalibration)
        self.menuReiceive_Material.addAction(self.actionMachine_Capability)
        self.menuReiceive_Material.addAction(self.actionSPC)
        self.menuReiceive_Material.addAction(self.actionMSA)
        self.menuReiceive_Material.addAction(self.actionVender_Audits)
        self.menubar.addAction(self.menuCustomer_Details.menuAction())
        self.menubar.addAction(self.menuQMS.menuAction())
        self.menubar.addAction(self.menuPart_Production_Calculator.menuAction())
        self.menubar.addAction(self.menuReiceive_Material.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.WebScrapingtool)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPPC)
        self.toolBar.addAction(self.actionPDIR)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEXCELToPDF)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        end_time=time.time()
        total_time=end_time-start_time
        print("done in :",total_time)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Q-LOOP"))
        self.menuCustomer_Details.setTitle(_translate("MainWindow", "Customer Details   "))
        self.menuQMS.setTitle(_translate("MainWindow", "QMS   "))
        self.menuNon_Conformance.setTitle(_translate("MainWindow", "Non-Conformance"))
        self.menuPart_Production_Calculator.setTitle(_translate("MainWindow", "Part Production Calculator   "))
        self.menuAbout.setTitle(_translate("MainWindow", "About   "))
        self.menuReiceive_Material.setTitle(_translate("MainWindow", "Plans   "))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionEnter_Customer_Details.setText(_translate("MainWindow", "Enter and Edit Customer Details"))
        self.actionSearch_Customer_Details.setText(_translate("MainWindow", "Search Customer Details"))
        self.actionPDIR.setText(_translate("MainWindow", "PDIR"))
        self.actionCustomer.setText(_translate("MainWindow", "Customer"))
        self.actionInhouse.setText(_translate("MainWindow", "Inhouse"))
        self.actionCalibration.setText(_translate("MainWindow", "Calibration"))
        self.actionMachine_Capability.setText(_translate("MainWindow", "Machine Capability"))
        self.actionSPC.setText(_translate("MainWindow", "SPC"))
        self.actionMSA.setText(_translate("MainWindow", "MSA"))
        self.actionVender_Audits.setText(_translate("MainWindow", "Vender Audits"))
        self.actionPPC.setText(_translate("MainWindow", "PPC"))
        self.WebScrapingtool.setText(_translate("MainWindow", "Web Scraping tool"))
        self.WebScrapingtool.setToolTip(_translate("MainWindow", "Web Scraping tool"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionEXCELToPDF.setText(_translate("MainWindow", "EXCELtoPDF"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

