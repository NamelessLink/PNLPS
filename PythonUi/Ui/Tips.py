# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tips.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_Tips(object):
    def setupUi(self, Tips):
        Tips.setObjectName("Tips")
        Tips.resize(325, 173)
        # Tips.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.label = QtWidgets.QLabel(Tips)
        self.label.setGeometry(QtCore.QRect(10, 0, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Tips)
        self.pushButton.setGeometry(QtCore.QRect(130, 100, 71, 31))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                        "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                        )


        self.retranslateUi(Tips)
        QtCore.QMetaObject.connectSlotsByName(Tips)

    def retranslateUi(self, Tips):
        _translate = QtCore.QCoreApplication.translate
        Tips.setWindowTitle(_translate("Tips", "提示信息"))
        self.label.setText(_translate("Tips", "提示信息"))
        self.pushButton.setText(_translate("Tips", "确定"))


