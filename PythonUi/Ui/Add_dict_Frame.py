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
        Add_dict_Frame.resize(625, 438)
        Add_dict_Frame.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(Add_dict_Frame)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 210, 351, 31))
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
        self.label_2.setGeometry(QtCore.QRect(90, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 370, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 370, 71, 31))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.Close_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Close_Button.setGeometry(QtCore.QRect(585, 10, 30, 30))
        self.Close_Button.setObjectName("Close_Button")
        self.Close_Button.setStyleSheet("QPushButton{border-image: url(./Ui/exit.png)}"
                                        "QPushButton:hover{background-color: red;border-image: url(./Ui/exit.png)}"
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




