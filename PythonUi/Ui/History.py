# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'History.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QAbstractItemView


class Ui_History(object):
    def setupUi(self, History):
        History.setObjectName("History")
        History.resize(625, 438)
        History.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        History.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.centralwidget = QtWidgets.QWidget(History)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;background:white;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")

        self.tableWidget = QtWidgets.QTableWidget(History)
        self.tableWidget.setGeometry(QtCore.QRect(50, 60, 531, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 125)
        self.tableWidget.setColumnWidth(1, 399)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(270, 380, 81, 41))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                      "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                      )
        History.setCentralWidget(self.centralwidget)

        self.retranslateUi(History)
        QtCore.QMetaObject.connectSlotsByName(History)

    def retranslateUi(self, History):
        _translate = QtCore.QCoreApplication.translate
        History.setWindowTitle(_translate("History", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("History", "时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("History", "文本"))
        self.closeButton.setText(_translate("History", "关闭"))
        self.label.setText(_translate("History", "最近历史记录"))

