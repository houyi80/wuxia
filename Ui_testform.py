# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\wuxia\testform.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.infoBox = QtWidgets.QTextBrowser(Form)
        self.infoBox.setGeometry(QtCore.QRect(10, 301, 461, 261))
        self.infoBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.infoBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.infoBox.setObjectName("infoBox")
        self.pb_time = QtWidgets.QProgressBar(Form)
        self.pb_time.setGeometry(QtCore.QRect(10, 570, 211, 23))
        self.pb_time.setProperty("value", 24)
        self.pb_time.setObjectName("pb_time")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
