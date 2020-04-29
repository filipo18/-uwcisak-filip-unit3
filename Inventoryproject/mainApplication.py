import csv
from csv import writer
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog, QTableWidgetItem, QMessageBox, QTableWidget
import mylib

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
        self.tableWidget.cellChanged.connect(self.changeDB)
        self.butt_save.clicked.connect(self.save)
        self.butt_reset.clicked.connect(self.cancel)

        loginVar = LoginApp(self)
        loginVar.show()
        # This is a behaviour for buttons for main app window
        self.butt_logout.clicked.connect(self.exitFunc)


    # this is a method for changing table widget
    def changeDB(self):
        item = self.tableWidget.currentItem()  # cell clicked
        row = self.tableWidget.currentRow()  # row clicked
        col = self.tableWidget.currentColumn()  # column selected
        # change the color of the cell clicked
        self.tableWidget.item(row, col).setBackground(QtGui.QColor(100, 100, 150))
        # show the item in the terminal for debuging
        print(item.text())
        print(item)
        self.butt_save.setDisabled(False)
        self.butt_reset.setDisabled(False)

    def save(self):
        print("Save to CSV File")
        first = ['id', 'name', 'type', 'color', 'type_of_wood', 'borrowed', 'returned']
        id = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
        name = [self.tableWidget.item(row, 1).text() for row in range(self.tableWidget.rowCount())]
        type = [self.tableWidget.item(row, 2).text() for row in range(self.tableWidget.rowCount())]
        color = [self.tableWidget.item(row, 3).text() for row in range(self.tableWidget.rowCount())]
        type_of_wood = [self.tableWidget.item(row, 4).text() for row in range(self.tableWidget.rowCount())]
        borrowed = [self.tableWidget.item(row, 5).text() for row in range(self.tableWidget.rowCount())]
        returned = [self.tableWidget.item(row, 6).text() for row in range(self.tableWidget.rowCount())]
        table = [id, name, type, color, type_of_wood, borrowed, returned]

        row_list = list(zip(*table))
        with open('db.csv', 'w', newline='') as database:
            writer = csv.writer(database)
            writer.writerows(row_list)

    def cancel(self):
        self.load_data()

    # data base, read comma-separated values file
    def load_data(self):
        data = []
        with open('db.csv') as mydatabase:
            file = csv.reader(mydatabase, delimiter=",")
            for i, row in enumerate(file):
                for j, col in enumerate(row):
                    data.append([i, j, col])
                    self.tableWidget.setItem(i, j, QTableWidgetItem(col))

        return[]

    # Button functions
    def addFunc(self):
        addVar = AddApp(self)
        addVar.show()

    def deleteFunc(self):
        deleteVar = DeleteApp(self)
        deleteVar.show()


    def exitFunc(self):
        sys.exit(0)


class LoginApp(loginW):
    def __init__(self, parent=None):
        super(LoginApp, self).__init__(parent)
        self.setupUi(self)  # build UI

        # This is a behaviour for exit button
        self.butt_exit.clicked.connect(self.exitFunc)
        self.butt_registration.clicked.connect(self.regFunc)
        self.butt_login.clicked.connect(self.try_login)

    def try_login(self):
        username = self.enter_username.text()
        password = self.enter_password.text()
        with open("Output.txt", "r") as output_file:
            for line in output_file:
                if mylib.verify_password(line, username + password):
                    self.close()
                    return
            QMessageBox.about(self, "Error", "Error: Wrong password")  # showing error message if password wrong
            self.enter_password.clear()
            self.enter_username.clear()


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
        if self.validate_registration():
            self.store()

    def validate_email(self):
        email = self.input_email.text()
        if '@' in email:
            self.input_email.setStyleSheet("border: 2px solid green")
            QMessageBox.about(self, "Error", "Error: Enter valid email")
            return True
        self.input_email.setStyleSheet("border: 2px solid red")
        return False

    def validate_name(self):
        name = self.input_username.text()
        if name.isalpha() and len(name) > 5:
            self.input_username.setStyleSheet("border: 2px solid green")
            return True
        self.input_username.setStyleSheet("border: 2px solid red")
        QMessageBox.about(self, "Error", "Error: Include only letters, password must be longer than 5 characters")
        return False

    def validate_password(self):
        password = self.input_password.text()
        password_conf = self.input_confpassword.text()
        if password != password_conf or len(password) < 5:
            self.input_password.setStyleSheet("border: 2px solid red")
            self.input_confpassword.setStyleSheet("border: 2px solid red")
            QMessageBox.about(self, "Error", "Error: Password is not longer than 5 or passwords don't match")
            return False
        self.input_password.setStyleSheet("border: 2px solid green")
        self.input_confpassword.setStyleSheet("border: 2px solid green")
        return True

    def validate_registration(self):
        email = self.validate_email()
        name = self.validate_name()
        password = self.validate_password()
        return email and name and password

    def store(self):
        email = self.input_email.text()
        username = self.input_username.text()
        password = self.input_password.text()
        print("Hashing,", email + password)
        msgE = mylib.hash_password(email + password)
        msgU = mylib.hash_password(username + password)
        with open('Output.txt', "a") as output_file:
            output_file.write('{}\n'.format(msgE))
            output_file.write('{}\n'.format(msgU))
        self.close()


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