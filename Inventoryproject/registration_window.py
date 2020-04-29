# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regform.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class RegisterWindow(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 269)
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(100, 30, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(60, 60, 211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.butt_exit = QtWidgets.QPushButton(Dialog)
        self.butt_exit.setGeometry(QtCore.QRect(80, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.butt_exit.setFont(font)
        self.butt_exit.setObjectName("butt_exit")
        self.butt_register = QtWidgets.QPushButton(Dialog)
        self.butt_register.setGeometry(QtCore.QRect(160, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.butt_register.setFont(font)
        self.butt_register.setObjectName("butt_register")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 80, 171, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_email = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.input_email.setFont(font)
        self.input_email.setStyleSheet("border: 2px solid red")
        self.input_email.setText("")
        self.input_email.setCursorPosition(0)
        self.input_email.setObjectName("input_email")
        self.verticalLayout.addWidget(self.input_email)
        self.input_username = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.input_username.setFont(font)
        self.input_username.setText("")
        self.input_username.setObjectName("input_username")
        self.verticalLayout.addWidget(self.input_username)
        self.input_password = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.input_password.setFont(font)
        self.input_password.setText("")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.verticalLayout.addWidget(self.input_password)
        self.input_confpassword = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.input_confpassword.setFont(font)
        self.input_confpassword.setText("")
        self.input_confpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_confpassword.setObjectName("input_confpassword")
        self.verticalLayout.addWidget(self.input_confpassword)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "REGISTRATION"))
        self.butt_exit.setText(_translate("Dialog", "Exit"))
        self.butt_register.setText(_translate("Dialog", "Register"))
        self.input_email.setPlaceholderText(_translate("Dialog", "Email"))
        self.input_username.setPlaceholderText(_translate("Dialog", "Username"))
        self.input_password.setPlaceholderText(_translate("Dialog", "Password"))
        self.input_confpassword.setPlaceholderText(_translate("Dialog", "Confirm Password"))
