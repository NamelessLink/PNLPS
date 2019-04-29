# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_dict_Frame.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_dict_Frame(object):
    def setupUi(self, Add_dict_Frame):
        Add_dict_Frame.setObjectName("Add_dict_Frame")
        Add_dict_Frame.resize(625, 438)
        self.centralwidget = QtWidgets.QWidget(Add_dict_Frame)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 210, 351, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 370, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 370, 71, 31))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 260, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        Add_dict_Frame.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_dict_Frame)
        QtCore.QMetaObject.connectSlotsByName(Add_dict_Frame)

    def retranslateUi(self, Add_dict_Frame):
        _translate = QtCore.QCoreApplication.translate
        Add_dict_Frame.setWindowTitle(_translate("Add_dict_Frame", "MainWindow"))
        self.label.setText(_translate("Add_dict_Frame", "词组入库功能"))
        self.label_2.setText(_translate("Add_dict_Frame", "输入词组："))
        self.pushButton.setText(_translate("Add_dict_Frame", "取消"))
        self.pushButton_2.setText(_translate("Add_dict_Frame", "确定"))
        self.label_3.setText(_translate("Add_dict_Frame", "输入格式：词 词频 词性（即三个属性以空格隔开）"))


