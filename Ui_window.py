# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_window.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):

    def setupUi(self, window):
        print("__set_win__")
        window.setObjectName("window")
        window.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.menu = QtWidgets.QWidget(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 0, 151, 581))
        self.menu.setStyleSheet("QWidget#menu{\n"
"background-color:rgb(66, 75, 111);\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"padding: 3px;\n"
"min-height: 60px;\n"
"background-color:rgb(66, 75, 111);\n"
"color: rgb(235, 235, 235)\n"
"}\n"
"QPushButton:hover{\n"
"border:none;\n"
"padding: 3px;\n"
"min-height: 60px;\n"
"background-color:rgb(87, 100, 156);\n"
"color:rgb(234, 234, 234);\n"
"font-size:15px\n"
"}\n"
"QPushButton:checked{\n"
"border:none;\n"
"padding: 3px;\n"
"min-height: 60px;\n"
"background-color:rgb(73, 74, 90);\n"
"color:rgb(234, 234, 234);\n"
"font-size:15px\n"
"}\n"
"")
        self.menu.setObjectName("menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout.setContentsMargins(0, 60, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pac_pbt = QtWidgets.QPushButton(self.menu)
        self.pac_pbt.setObjectName("pac_pbt")
        self.verticalLayout.addWidget(self.pac_pbt)
        self.app_pbt = QtWidgets.QPushButton(self.menu)
        self.app_pbt.setObjectName("app_pbt")
        self.verticalLayout.addWidget(self.app_pbt)
        self.map_pbt = QtWidgets.QPushButton(self.menu)
        self.map_pbt.setObjectName("map_pbt")
        self.verticalLayout.addWidget(self.map_pbt)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(150, 0, 451, 581))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"background-color:rgb(205, 206, 222);\n"
"color:rgb(88, 83, 127);\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"border-radius: 3px;\n"
"padding: 3px;\n"
"min-width: 60px;\n"
"background-color:rgb(113, 135, 167);\n"
"color: rgb(235, 235, 235);\n"
"}\n"
"QPushButton:hover{\n"
"border:none;\n"
"padding: 3px;\n"
"min-width: 60px;\n"
"background-color:rgb(146, 171, 208);\n"
"color:rgb(234, 234, 234);\n"
"}\n"
"QPushButton:disabled{\n"
"border:none;\n"
"padding: 3px;\n"
"min-height: 60px;\n"
"background-color:rgb(73, 74, 90);\n"
"}\n"
"QLineEdit{\n"
"border: 1px solid rgb(88, 83, 127);\n"
"border-radius: 3px;\n"
"padding: 3px;\n"
"\n"
"color: rgb(88, 83, 127);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(148, 81, 108);\n"
"border-radius: 3px;\n"
"padding: 3px;\n"
"\n"
"color: rgb(194, 124, 123);\n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 421, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pbt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pbt.setMinimumSize(QtCore.QSize(66, 0))
        self.pbt.setObjectName("pbt")
        self.horizontalLayout.addWidget(self.pbt)
        self.treeWidget = QtWidgets.QTreeWidget(self.page)
        self.treeWidget.setGeometry(QtCore.QRect(20, 340, 421, 221))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(20, 310, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 421, 231))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.chart_widget = QtWidgets.QWidget(self.page_2)
        self.chart_widget.setGeometry(QtCore.QRect(40, 40, 381, 501))
        self.chart_widget.setObjectName("chart_widget")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.map_label = QtWidgets.QLabel(self.page_3)
        self.map_label.setGeometry(QtCore.QRect(60, 60, 341, 461))
        self.map_label.setObjectName("map_label")
        self.stackedWidget.addWidget(self.page_3)
        window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.groubbtn = QtWidgets.QButtonGroup()
        self.groubbtn.addButton(self.pac_pbt, 0)
        self.groubbtn.addButton(self.app_pbt, 1)
        self.groubbtn.addButton(self.map_pbt, 2)
        self.pac_pbt.setCheckable(True)
        self.map_pbt.setCheckable(True)
        self.app_pbt.setCheckable(True)

        self.retranslateUi(window)
        self.stackedWidget.setCurrentIndex(0)
        self.pbt.setEnabled(False)


        self.lineEdit.textChanged['QString'].connect(window.isLineEditEmpty)
        self.pbt.clicked.connect(window.capt)
        self.groubbtn.buttonClicked['int'].connect(window.showPage)
        # self.pac_pbt.clicked.connect(window.showPage)
        # self.app_pbt.clicked.connect(window.showPage)
        # self.map_pbt.clicked.connect(window.showPage)
        QtCore.QMetaObject.connectSlotsByName(window)
        
    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "计算机网络课程设计——流量嗅探器"))
        self.pac_pbt.setText(_translate("window", "抓包分析"))
        self.app_pbt.setText(_translate("window", "应用流量监控"))
        self.map_pbt.setText(_translate("window", "看看谁在与我通信"))
        self.label.setText(_translate("window", "请输入网卡设备名称"))
        self.pbt.setText(_translate("window", "抓包"))
        self.map_label.setText(_translate("window", "map"))

