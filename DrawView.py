# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DrawView.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchCusto(object):
    def setupUi(self, SearchCusto):
        SearchCusto.setObjectName("SearchCusto")
        SearchCusto.setWindowModality(QtCore.Qt.WindowModal)
        SearchCusto.setEnabled(True)
        SearchCusto.resize(731, 652)
        SearchCusto.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        SearchCusto.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(SearchCusto)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 621, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 20, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 70, 691, 561))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 689, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 540, 701, 21))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(670, 0, 21, 541))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.graphicsView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 671, 541))
        self.graphicsView.setObjectName("graphicsView")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        SearchCusto.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SearchCusto)
        self.statusbar.setObjectName("statusbar")
        SearchCusto.setStatusBar(self.statusbar)

        self.retranslateUi(SearchCusto)
        QtCore.QMetaObject.connectSlotsByName(SearchCusto)

    def retranslateUi(self, SearchCusto):
        _translate = QtCore.QCoreApplication.translate
        SearchCusto.setWindowTitle(_translate("SearchCusto", "Search Customer Details"))
        self.pushButton.setText(_translate("SearchCusto", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchCusto = QtWidgets.QMainWindow()
    ui = Ui_SearchCusto()
    ui.setupUi(SearchCusto)
    SearchCusto.show()
    sys.exit(app.exec_())

