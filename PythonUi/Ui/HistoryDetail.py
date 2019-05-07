# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HistoryDetail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_HistoryDetail(object):
    def setupUi(self, HistoryDetail):
        HistoryDetail.setObjectName("HistoryDetail")
        HistoryDetail.resize(1060, 746)
        HistoryDetail.setFixedSize(1060, 746)
        HistoryDetail.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)


        self.closeButton = QtWidgets.QPushButton(HistoryDetail)
        self.closeButton.setGeometry(QtCore.QRect(460, 640, 162, 82))
        self.closeButton.setObjectName("closeButton")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}"
                                      "QPushButton:hover{border:2px groove black;border-radius:10px;padding:2px 4px;}"
                                      )

        self.textEdit = QtWidgets.QTextEdit(HistoryDetail)
        self.textEdit.setGeometry(QtCore.QRect(40, 80, 982, 542))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(1)
        self.textEdit.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.textEdit.setFont(font)

        self.label = QtWidgets.QLabel(HistoryDetail)
        self.label.setGeometry(QtCore.QRect(40, 10, 162, 62))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(HistoryDetail)
        QtCore.QMetaObject.connectSlotsByName(HistoryDetail)

    def retranslateUi(self, HistoryDetail):
        _translate = QtCore.QCoreApplication.translate
        HistoryDetail.setWindowTitle(_translate("HistoryDetail", "详细信息"))
        self.closeButton.setText(_translate("HistoryDetail", "关闭"))
        self.label.setText(_translate("HistoryDetail", "详细信息"))


