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
        History.resize(1250, 876)
        History.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        History.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.centralwidget = QtWidgets.QWidget(History)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;background:white;")
        self.label = QtWidgets.QLabel(History)
        self.label.setGeometry(QtCore.QRect(40, 20, 444, 62))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.tableWidget = QtWidgets.QTableWidget(History)
        self.tableWidget.setGeometry(QtCore.QRect(100, 120, 1062, 582))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 810)
        self.tableWidget.setRowCount(18)
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
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.tableWidget.setFont(font)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(540, 760, 162, 82))
        self.closeButton.setObjectName("closeButton")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(30)
        self.closeButton.setFont(font)
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

