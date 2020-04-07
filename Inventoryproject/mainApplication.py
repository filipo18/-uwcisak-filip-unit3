import csv
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog, QTableWidgetItem

from mainprogram import mainWindow as mainW
from login_window import LoginWindow as loginW
from add_window import AddWindow as addW
from delete_window import DeleteWindow as deleteW
from edit_window import EditWindow as editW
from lend_window import LendWindow as lendW
from return_window import ReturnWindow as returnW
from registration_window import RegisterWindow as regW


class MainWindowApp(QMainWindow, mainW):
    def __init__(self, parent=None):
        super(MainWindowApp, self).__init__(parent)
        self.setupUi(self)  # build UI
        self.data = self.load_data()

        loginVar = LoginApp(self)
        loginVar.show()

        # This is a behaviour for buttons for main app window
        self.butt_addguitar.clicked.connect(self.addFunc)
        self.butt_edit.clicked.connect(self.editFunc)
        self.butt_lend.clicked.connect(self.lendFunc)
        self.butt_logout.clicked.connect(self.exitFunc)
        self.butt_remove.clicked.connect(self.deleteFunc)
        self.butt_return.clicked.connect(self.returnguitarFunc)

    # data base, read comma-separated values file
    def load_data(self):
        data = []
        with open('db.csv') as mydatabase:
            file = csv.reader(mydatabase, delimiter=",")
            for i, row in enumerate(file):
                for j, col in enumerate(row):
                    if i != 0:  # We don't show the first line
                        data.append([i, j, col])
                        self.tableWidget.setItem(i, j, QTableWidgetItem(col))

        return[]

    # Button functions
    def addFunc(self):
        addVar = AddApp(self)
        addVar.show()

    def editFunc(self):
        editVar = EditApp(self)
        editVar.show()

    def deleteFunc(self):
        deleteVar = DeleteApp(self)
        deleteVar.show()

    def lendFunc(self):
        lendVar = LendApp(self)
        lendVar.show()

    def returnguitarFunc(self):
        returnVar = ReturnApp(self)
        returnVar.show()

    def exitFunc(self):
        sys.exit(0)


class LoginApp(loginW):
    def __init__(self, parent=None):
        super(LoginApp, self).__init__(parent)
        self.setupUi(self)  # build UI

        # This is a behaviour for exit button
        self.butt_exit.clicked.connect(self.exitFunc)
        self.butt_registration.clicked.connect(self.regFunc)

    def exitFunc(self):
        sys.exit(0)  # 0 means exit without errors

    # This opens registration form
    def regFunc(self):
        regVar = RegisterApp(self)
        regVar.show()


class RegisterApp(regW):
    def __init__(self, parent=None):
        super(RegisterApp, self).__init__(parent)
        self.setupUi(self)  # build UI

        self.butt_exit.clicked.connect(self.exitFunc)
        self.butt_register.clicked.connect(self.try_regFunc)

    def exitFunc(self):
        sys.exit(0)

    def try_regFunc(self):
        email = self.input_email.text()
        if '@' not in email:
            self.input_email.setStyleSheet("border: 2px solid red")
        else:
            self.input_email.setStyleSheet("border: 2px solid green")


class AddApp(addW):
    def __init__(self, parent=None):
        super(AddApp, self).__init__(parent)
        self.setupUi(self)  # build UI


class DeleteApp(deleteW):
    def __init__(self, parent=None):
        super(DeleteApp, self).__init__(parent)
        self.setupUi(self)  # Build UI


class EditApp(editW):
    def __init__(self, parent=None):
        super(EditApp, self).__init__(parent)
        self.setupUi(self)  # Build UI


class LendApp(lendW):
    def __init__(self, parent=None):
        super(LendApp, self).__init__(parent)
        self.setupUi(self)  # Build UI


class ReturnApp(returnW):
    def __init__(self, parent=None):
        super(ReturnApp, self).__init__(parent)
        self.setupUi(self)  # build UI


app = QApplication(sys.argv)
mainW = MainWindowApp() # Create the object of the main window
mainW.show()
app.exec_()