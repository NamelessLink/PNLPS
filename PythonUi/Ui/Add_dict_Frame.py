# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_dict_Frame.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_Add_dict_Frame(object):
    def setupUi(self, Add_dict_Frame):
        Add_dict_Frame.setObjectName("Add_dict_Frame")
        Add_dict_Frame.resize(1250, 876)
        Add_dict_Frame.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        Add_dict_Frame.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.centralwidget = QtWidgets.QWidget(Add_dict_Frame)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;background:white;")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(440, 420, 702, 62))
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(30)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.label = QtWidgets.QLabel(Add_dict_Frame)
        self.label.setGeometry(QtCore.QRect(60, 80, 382, 122))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Add_dict_Frame)
        self.label_2.setGeometry(QtCore.QRect(180, 420, 242, 62))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 740, 142, 62))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 740, 142, 62))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.Close_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Close_Button.setGeometry(QtCore.QRect(1170, 20, 60, 60))
        self.Close_Button.setObjectName("Close_Button")
        self.Close_Button.setStyleSheet("QPushButton{border-image: url(exit.png)}"
                                        "QPushButton:hover{background-color: red;border-image: url(exit.png)}"
                                        )

        Add_dict_Frame.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_dict_Frame)
        QtCore.QMetaObject.connectSlotsByName(Add_dict_Frame)

    def retranslateUi(self, Add_dict_Frame):
        _translate = QtCore.QCoreApplication.translate
        Add_dict_Frame.setWindowTitle(_translate("Add_dict_Frame", "词组入库"))
        self.label.setText(_translate("Add_dict_Frame", "词组入库功能"))
        self.label_2.setText(_translate("Add_dict_Frame", "输入词组："))
        self.pushButton.setText(_translate("Add_dict_Frame", "取消"))
        self.pushButton_2.setText(_translate("Add_dict_Frame", "确定"))




