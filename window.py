# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 925)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.row2col1 = QtWidgets.QGroupBox(self.centralwidget)
        self.row2col1.setTitle("")
        self.row2col1.setObjectName("row2col1")
        self.gridLayout.addWidget(self.row2col1, 1, 0, 1, 1)
        self.row5col2 = QtWidgets.QGroupBox(self.centralwidget)
        self.row5col2.setTitle("")
        self.row5col2.setObjectName("row5col2")
        self.gridLayout.addWidget(self.row5col2, 4, 1, 1, 1)
        self.menu = QtWidgets.QGroupBox(self.centralwidget)
        self.menu.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setStyleSheet("")
        self.menu.setTitle("")
        self.menu.setFlat(False)
        self.menu.setObjectName("menu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.col1 = QtWidgets.QGroupBox(self.menu)
        self.col1.setTitle("")
        self.col1.setObjectName("col1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.col1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.col1Gray = QtWidgets.QPushButton(self.col1)
        self.col1Gray.setStyleSheet("background-color: gray")
        self.col1Gray.setText("")
        self.col1Gray.setObjectName("col1Gray")
        self.verticalLayout.addWidget(self.col1Gray)
        self.col1Orange = QtWidgets.QPushButton(self.col1)
        self.col1Orange.setStyleSheet("background-color: orange")
        self.col1Orange.setText("")
        self.col1Orange.setObjectName("col1Orange")
        self.verticalLayout.addWidget(self.col1Orange)
        self.col1Green = QtWidgets.QPushButton(self.col1)
        self.col1Green.setStyleSheet("background-color: green")
        self.col1Green.setText("")
        self.col1Green.setObjectName("col1Green")
        self.verticalLayout.addWidget(self.col1Green)
        self.horizontalLayout.addWidget(self.col1)
        self.col2 = QtWidgets.QGroupBox(self.menu)
        self.col2.setTitle("")
        self.col2.setObjectName("col2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.col2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.col2Gray = QtWidgets.QPushButton(self.col2)
        self.col2Gray.setStyleSheet("background-color: gray")
        self.col2Gray.setText("")
        self.col2Gray.setObjectName("col2Gray")
        self.verticalLayout_5.addWidget(self.col2Gray)
        self.col2Orange = QtWidgets.QPushButton(self.col2)
        self.col2Orange.setStyleSheet("background-color: orange")
        self.col2Orange.setText("")
        self.col2Orange.setObjectName("col2Orange")
        self.verticalLayout_5.addWidget(self.col2Orange)
        self.col2Green = QtWidgets.QPushButton(self.col2)
        self.col2Green.setStyleSheet("background-color: green")
        self.col2Green.setText("")
        self.col2Green.setObjectName("col2Green")
        self.verticalLayout_5.addWidget(self.col2Green)
        self.horizontalLayout.addWidget(self.col2)
        self.col3 = QtWidgets.QGroupBox(self.menu)
        self.col3.setTitle("")
        self.col3.setObjectName("col3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.col3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.col3Gray = QtWidgets.QPushButton(self.col3)
        self.col3Gray.setStyleSheet("background-color: gray")
        self.col3Gray.setText("")
        self.col3Gray.setObjectName("col3Gray")
        self.verticalLayout_4.addWidget(self.col3Gray)
        self.col3Orange = QtWidgets.QPushButton(self.col3)
        self.col3Orange.setStyleSheet("background-color: orange")
        self.col3Orange.setText("")
        self.col3Orange.setObjectName("col3Orange")
        self.verticalLayout_4.addWidget(self.col3Orange)
        self.col3Green = QtWidgets.QPushButton(self.col3)
        self.col3Green.setStyleSheet("background-color: green")
        self.col3Green.setText("")
        self.col3Green.setObjectName("col3Green")
        self.verticalLayout_4.addWidget(self.col3Green)
        self.horizontalLayout.addWidget(self.col3)
        self.col4 = QtWidgets.QGroupBox(self.menu)
        self.col4.setTitle("")
        self.col4.setObjectName("col4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.col4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.col4Gray = QtWidgets.QPushButton(self.col4)
        self.col4Gray.setStyleSheet("background-color: gray")
        self.col4Gray.setText("")
        self.col4Gray.setObjectName("col4Gray")
        self.verticalLayout_3.addWidget(self.col4Gray)
        self.col4Orange = QtWidgets.QPushButton(self.col4)
        self.col4Orange.setStyleSheet("background-color: orange")
        self.col4Orange.setText("")
        self.col4Orange.setObjectName("col4Orange")
        self.verticalLayout_3.addWidget(self.col4Orange)
        self.col4Green = QtWidgets.QPushButton(self.col4)
        self.col4Green.setStyleSheet("background-color: green")
        self.col4Green.setText("")
        self.col4Green.setObjectName("col4Green")
        self.verticalLayout_3.addWidget(self.col4Green)
        self.horizontalLayout.addWidget(self.col4)
        self.col55 = QtWidgets.QGroupBox(self.menu)
        self.col55.setTitle("")
        self.col55.setObjectName("col55")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.col55)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.col5Gray = QtWidgets.QPushButton(self.col55)
        self.col5Gray.setStyleSheet("background-color: gray")
        self.col5Gray.setText("")
        self.col5Gray.setObjectName("col5Gray")
        self.verticalLayout_2.addWidget(self.col5Gray)
        self.col5Orange = QtWidgets.QPushButton(self.col55)
        self.col5Orange.setStyleSheet("background-color: orange")
        self.col5Orange.setText("")
        self.col5Orange.setObjectName("col5Orange")
        self.verticalLayout_2.addWidget(self.col5Orange)
        self.col5Green = QtWidgets.QPushButton(self.col55)
        self.col5Green.setStyleSheet("background-color: green")
        self.col5Green.setText("")
        self.col5Green.setObjectName("col5Green")
        self.verticalLayout_2.addWidget(self.col5Green)
        self.horizontalLayout.addWidget(self.col55)
        self.gridLayout.addWidget(self.menu, 8, 0, 1, 5)
        self.row2col4 = QtWidgets.QGroupBox(self.centralwidget)
        self.row2col4.setTitle("")
        self.row2col4.setObjectName("row2col4")
        self.gridLayout.addWidget(self.row2col4, 1, 3, 1, 1)
        self.row1col2 = QtWidgets.QGroupBox(self.centralwidget)
        self.row1col2.setTitle("")
        self.row1col2.setObjectName("row1col2")
        self.gridLayout.addWidget(self.row1col2, 0, 1, 1, 1)
        self.row6col3 = QtWidgets.QGroupBox(self.centralwidget)
        self.row6col3.setTitle("")
        self.row6col3.setObjectName("row6col3")
        self.gridLayout.addWidget(self.row6col3, 5, 2, 1, 1)
        self.row3col4 = QtWidgets.QGroupBox(self.centralwidget)
        self.row3col4.setTitle("")
        self.row3col4.setObjectName("row3col4")
        self.gridLayout.addWidget(self.row3col4, 2, 3, 1, 1)
        self.row2col3 = QtWidgets.QGroupBox(self.centralwidget)
        self.row2col3.setTitle("")
        self.row2col3.setObjectName("row2col3")
        self.gridLayout.addWidget(self.row2col3, 1, 2, 1, 1)
        self.row4col4 = QtWidgets.QGroupBox(self.centralwidget)
        self.row4col4.setTitle("")
        self.row4col4.setObjectName("row4col4")
        self.gridLayout.addWidget(self.row4col4, 3, 3, 1, 1)
        self.row5col3 = QtWidgets.QGroupBox(self.centralwidget)
        self.row5col3.setTitle("")
        self.row5col3.setObjectName("row5col3")
        self.gridLayout.addWidget(self.row5col3, 4, 2, 1, 1)
        self.row6col5 = QtWidgets.QGroupBox(self.centralwidget)
        self.row6col5.setTitle("")
        self.row6col5.setObjectName("row6col5")
        self.gridLayout.addWidget(self.row6col5, 5, 4, 1, 1)
        self.row5col4 = QtWidgets.QGroupBox(self.centralwidget)
        self.row5col4.setTitle("")
        self.row5col4.setObjectName("row5col4")
        self.gridLayout.addWidget(self.row5col4, 4, 3, 1, 1)
        self.row5col1 = QtWidgets.QGroupBox(self.centralwidget)
        self.row5col1.setTitle("")
        self.row5col1.setObjectName("row5col1")
        self.gridLayout.addWidget(self.row5col1, 4, 0, 1, 1)
        self.row3col3 = QtWidgets.QGroupBox(self.centralwidget)
        self.row3col3.setTitle("")
        self.row3col3.setObjectName("row3col3")
        self.gridLayout.addWidget(self.row3col3, 2, 2, 1, 1)
        self.row1col3 = QtWidgets.QGroupBox(self.centralwidget)
        self.row1col3.setTitle("")
        self.row1col3.setObjectName("row1col3")
        self.gridLayout.addWidget(self.row1col3, 0, 2, 1, 1)
        self.row1col4 = QtWidgets.QGroupBox(self.centralwidget)
        self.row1col4.setTitle("")
        self.row1col4.setObjectName("row1col4")
        self.gridLayout.addWidget(self.row1col4, 0, 3, 1, 1)
        self.row5col5 = QtWidgets.QGroupBox(self.centralwidget)
        self.row5col5.setTitle("")
        self.row5col5.setObjectName("row5col5")
        self.gridLayout.addWidget(self.row5col5, 4, 4, 1, 1)
        self.row4col1 = QtWidgets.QGroupBox(self.centralwidget)
        self.row4col1.setTitle("")
        self.row4col1.setObjectName("row4col1")
        self.gridLayout.addWidget(self.row4col1, 3, 0, 1, 1)
        self.row3col1 = QtWidgets.QGroupBox(self.centralwidget)
        self.row3col1.setTitle("")
        self.row3col1.setObjectName("row3col1")
        self.gridLayout.addWidget(self.row3col1, 2, 0, 1, 1)
        self.row2col5 = QtWidgets.QGroupBox(self.centralwidget)
        self.row2col5.setTitle("")
        self.row2col5.setObjectName("row2col5")
        self.gridLayout.addWidget(self.row2col5, 1, 4, 1, 1)
        self.row2col2 = QtWidgets.QGroupBox(self.centralwidget)
        self.row2col2.setTitle("")
        self.row2col2.setObjectName("row2col2")
        self.gridLayout.addWidget(self.row2col2, 1, 1, 1, 1)
        self.row1col1 = QtWidgets.QGroupBox(self.centralwidget)
        self.row1col1.setTitle("")
        self.row1col1.setObjectName("row1col1")
        self.gridLayout.addWidget(self.row1col1, 0, 0, 1, 1)
        self.row6col1 = QtWidgets.QGroupBox(self.centralwidget)
        self.row6col1.setTitle("")
        self.row6col1.setObjectName("row6col1")
        self.gridLayout.addWidget(self.row6col1, 5, 0, 1, 1)
        self.row4col5 = QtWidgets.QGroupBox(self.centralwidget)
        self.row4col5.setTitle("")
        self.row4col5.setObjectName("row4col5")
        self.gridLayout.addWidget(self.row4col5, 3, 4, 1, 1)
        self.row4col3 = QtWidgets.QGroupBox(self.centralwidget)
        self.row4col3.setTitle("")
        self.row4col3.setObjectName("row4col3")
        self.gridLayout.addWidget(self.row4col3, 3, 2, 1, 1)
        self.row4col2 = QtWidgets.QGroupBox(self.centralwidget)
        self.row4col2.setTitle("")
        self.row4col2.setObjectName("row4col2")
        self.gridLayout.addWidget(self.row4col2, 3, 1, 1, 1)
        self.row3col5 = QtWidgets.QGroupBox(self.centralwidget)
        self.row3col5.setTitle("")
        self.row3col5.setObjectName("row3col5")
        self.gridLayout.addWidget(self.row3col5, 2, 4, 1, 1)
        self.row6col2 = QtWidgets.QGroupBox(self.centralwidget)
        self.row6col2.setTitle("")
        self.row6col2.setObjectName("row6col2")
        self.gridLayout.addWidget(self.row6col2, 5, 1, 1, 1)
        self.row1col5 = QtWidgets.QGroupBox(self.centralwidget)
        self.row1col5.setTitle("")
        self.row1col5.setObjectName("row1col5")
        self.gridLayout.addWidget(self.row1col5, 0, 4, 1, 1)
        self.row6col4 = QtWidgets.QGroupBox(self.centralwidget)
        self.row6col4.setTitle("")
        self.row6col4.setObjectName("row6col4")
        self.gridLayout.addWidget(self.row6col4, 5, 3, 1, 1)
        self.row3col2 = QtWidgets.QGroupBox(self.centralwidget)
        self.row3col2.setTitle("")
        self.row3col2.setObjectName("row3col2")
        self.gridLayout.addWidget(self.row3col2, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.doneBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doneBtn.sizePolicy().hasHeightForWidth())
        self.doneBtn.setSizePolicy(sizePolicy)
        self.doneBtn.setObjectName("doneBtn")
        self.gridLayout_2.addWidget(self.doneBtn, 0, 0, 1, 1)
        self.newBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newBtn.sizePolicy().hasHeightForWidth())
        self.newBtn.setSizePolicy(sizePolicy)
        self.newBtn.setObjectName("newBtn")
        self.gridLayout_2.addWidget(self.newBtn, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 9, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.doneBtn.setText(_translate("MainWindow", "Done"))
        self.newBtn.setText(_translate("MainWindow", "New word"))
