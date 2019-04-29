# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'File_Select.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_File_Select(object):
    def setupUi(self, File_Select):
        File_Select.setObjectName("File_Select")
        File_Select.resize(578, 322)
        self.label_2 = QtWidgets.QLabel(File_Select)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(File_Select)
        self.textEdit.setGeometry(QtCore.QRect(210, 130, 261, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(File_Select)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 240, 71, 31))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(File_Select)
        self.pushButton.setGeometry(QtCore.QRect(400, 240, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(File_Select)
        self.label.setGeometry(QtCore.QRect(30, 30, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(File_Select)
        self.toolButton.setGeometry(QtCore.QRect(480, 130, 31, 31))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(File_Select)
        QtCore.QMetaObject.connectSlotsByName(File_Select)

    def retranslateUi(self, File_Select):
        _translate = QtCore.QCoreApplication.translate
        File_Select.setWindowTitle(_translate("File_Select", "Form"))
        self.label_2.setText(_translate("File_Select", "文件路径："))
        self.pushButton_2.setText(_translate("File_Select", "确定"))
        self.pushButton.setText(_translate("File_Select", "取消"))
        self.label.setText(_translate("File_Select", "文件选择"))
        self.toolButton.setText(_translate("File_Select", "..."))



