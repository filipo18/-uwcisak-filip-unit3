# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class AddWindow(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        Dialog.setMinimumSize(QtCore.QSize(320, 240))
        Dialog.setMaximumSize(QtCore.QSize(320, 240))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 10, 191, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_addguitar = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_addguitar.setFont(font)
        self.text_addguitar.setObjectName("text_addguitar")
        self.verticalLayout.addWidget(self.text_addguitar)
        spacerItem = QtWidgets.QSpacerItem(18, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.enter_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.enter_name.setObjectName("enter_name")
        self.verticalLayout.addWidget(self.enter_name)
        spacerItem1 = QtWidgets.QSpacerItem(18, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.ente_type = QtWidgets.QLineEdit(self.layoutWidget)
        self.ente_type.setObjectName("ente_type")
        self.verticalLayout.addWidget(self.ente_type)
        spacerItem2 = QtWidgets.QSpacerItem(18, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.enter_color = QtWidgets.QLineEdit(self.layoutWidget)
        self.enter_color.setObjectName("enter_color")
        self.verticalLayout.addWidget(self.enter_color)
        spacerItem3 = QtWidgets.QSpacerItem(48, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.enter_wood_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.enter_wood_2.setObjectName("enter_wood_2")
        self.verticalLayout.addWidget(self.enter_wood_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.text_addguitar.setText(_translate("Dialog", "ADD GUITAR"))
        self.enter_name.setText(_translate("Dialog", "Name"))
        self.ente_type.setText(_translate("Dialog", "enter_type"))
        self.enter_color.setText(_translate("Dialog", "Color"))
        self.enter_wood_2.setText(_translate("Dialog", "Wood"))
