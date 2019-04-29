# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_Result(object):
    def setupUi(self, Result):
        Result.setObjectName("Result")
        Result.resize(625, 438)
        Result.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(Result)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 70, 541, 271))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(1)
        self.textEdit.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 370, 81, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 370, 81, 41))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )

        Result.setCentralWidget(self.centralwidget)
        self.retranslateUi(Result)
        QtCore.QMetaObject.connectSlotsByName(Result)

    def retranslateUi(self, Result):
        _translate = QtCore.QCoreApplication.translate
        Result.setWindowTitle(_translate("Result", "最终结果"))
        self.label.setText(_translate("Result", "结果："))
        self.pushButton.setText(_translate("Result", "退出"))
        self.pushButton_2.setText(_translate("Result", "主界面"))


