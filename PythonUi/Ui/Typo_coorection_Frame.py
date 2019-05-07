# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Typo_coorection_Frame.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QFileDialog


class Ui_Typo_coorection_Frame(object):
    def setupUi(self, Typo_coorection_Frame):
        Typo_coorection_Frame.setObjectName("Typo_coorection_Frame")
        Typo_coorection_Frame.resize(1250, 876)
        Typo_coorection_Frame.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        Typo_coorection_Frame.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.centralwidget = QtWidgets.QWidget(Typo_coorection_Frame)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;background:white;")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 540, 242, 62))
        self.pushButton_2.setObjectName("pushButton_2")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(26)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(480, 260, 702, 62))
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(30)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")

        self.label = QtWidgets.QLabel(Typo_coorection_Frame)
        self.label.setGeometry(QtCore.QRect(60, 80, 442, 102))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Typo_coorection_Frame)
        self.label_2.setGeometry(QtCore.QRect(60, 260, 402, 62))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Typo_coorection_Frame)
        self.label_3.setGeometry(QtCore.QRect(140, 380, 322, 62))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 740, 142, 62))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 740, 142, 62))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.Close_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Close_Button.setGeometry(QtCore.QRect(1170, 20, 60, 60))
        self.Close_Button.setObjectName("Close_Button")
        self.Close_Button.setStyleSheet("QPushButton{border-image: url(exit.png)}"
                                        "QPushButton:hover{background-color: red;border-image: url(exit.png)}"
                                        )

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(480, 380, 702, 62))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")

        Typo_coorection_Frame.setCentralWidget(self.centralwidget)

        self.retranslateUi(Typo_coorection_Frame)
        QtCore.QMetaObject.connectSlotsByName(Typo_coorection_Frame)

    def retranslateUi(self, Typo_coorection_Frame):
        _translate = QtCore.QCoreApplication.translate
        Typo_coorection_Frame.setWindowTitle(_translate("Typo_coorection_Frame", "错字纠正"))
        self.label.setText(_translate("Typo_coorection_Frame", "错别字纠正功能"))
        self.label_2.setText(_translate("Typo_coorection_Frame", "输入需要纠正文本："))
        self.label_3.setText(_translate("Typo_coorection_Frame", "输入文件路径："))
        self.pushButton_2.setText(_translate("Typo_coorection_Frame", "选择文件输入"))
        self.pushButton.setText(_translate("Typo_coorection_Frame", "取消"))
        self.pushButton_3.setText(_translate("Typo_coorection_Frame", "确定"))


