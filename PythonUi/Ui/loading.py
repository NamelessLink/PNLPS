# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(150, 150)
        Frame.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        Frame.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        Frame.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(25, 25, 100, 100))
        self.label.setObjectName("label")
        self.gif = QMovie("loading.gif")
        self.label.setMovie(self.gif)
        self.gif.start()
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))


