# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exit(object):
    def setupUi(self, Exit):
        Exit.setObjectName("Exit")
        Exit.resize(357, 213)
        Exit.setFixedSize(357, 213)
        Exit.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.label = QtWidgets.QLabel(Exit)
        self.label.setGeometry(QtCore.QRect(80, 40, 191, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Exit)
        self.pushButton.setGeometry(QtCore.QRect(70, 140, 71, 41))
        self.pushButton.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                      "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                      )

        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Exit)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 140, 71, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                      "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                      )

        self.retranslateUi(Exit)
        QtCore.QMetaObject.connectSlotsByName(Exit)

    def retranslateUi(self, Exit):
        _translate = QtCore.QCoreApplication.translate
        Exit.setWindowTitle(_translate("Exit", "Exit"))
        self.label.setText(_translate("Exit", "是否确认退出"))
        self.pushButton.setText(_translate("Exit", "是"))
        self.pushButton_2.setText(_translate("Exit", "否"))


