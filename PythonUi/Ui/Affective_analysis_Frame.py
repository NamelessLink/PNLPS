# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Affective_analysis_Frame.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets, Qt



class Ui_Affective_analysis_Frame(object):
    def setupUi(self, Affective_analysis_Frame):
        Affective_analysis_Frame.setObjectName("Affective_analysis_Frame")
        Affective_analysis_Frame.resize(625, 438)
        Affective_analysis_Frame.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.centralwidget = QtWidgets.QWidget(Affective_analysis_Frame)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 130, 351, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 270, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 370, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 370, 71, 31))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.Close_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Close_Button.setGeometry(QtCore.QRect(585, 10, 30, 30))
        self.Close_Button.setObjectName("Close_Button")
        self.Close_Button.setStyleSheet("QPushButton{border-image: url(./Ui/exit.png)}"
                                        "QPushButton:hover{background-color: red;border-image: url(./Ui/exit.png)}"
                                        )

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 190, 351, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")


        Affective_analysis_Frame.setCentralWidget(self.centralwidget)

        self.retranslateUi(Affective_analysis_Frame)
        QtCore.QMetaObject.connectSlotsByName(Affective_analysis_Frame)

    def retranslateUi(self, Affective_analysis_Frame):
        _translate = QtCore.QCoreApplication.translate
        Affective_analysis_Frame.setWindowTitle(_translate("Affective_analysis_Frame", "情感分析"))
        self.label.setText(_translate("Affective_analysis_Frame", "情感分析功能"))
        self.label_2.setText(_translate("Affective_analysis_Frame", "输入分析文本："))
        self.label_3.setText(_translate("Affective_analysis_Frame", "输入文件路径："))
        self.pushButton_2.setText(_translate("Affective_analysis_Frame", "选择文件输入"))
        self.pushButton.setText(_translate("Affective_analysis_Frame", "取消"))
        self.pushButton_3.setText(_translate("Affective_analysis_Frame", "确定"))
