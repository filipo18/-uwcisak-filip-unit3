Development 
============

## Design
Picture below shows how GUI of program will eventually look. Even though this is not compleatly final version, it is preatty close to how final version will look.

![GUI design](GUIdesign.png)

**Fig 2.** GUI design

When user enters his credentials home page opens. TAble of guitars is shown there. Buttons open dialog boxes for adding, removing, editing, lending and returning guitar.

## Registration

![Registration flow diagram](Login.jpg)

**Fig 1.** Registration flow diagram

This is ethod for secure log in where developer is not able to see password user has entered. We achive that by using ``` hashlib ``` and ```os``` librarys. Fisrt step in the flow diagram Fig 1. is to crate dictionary. Dictionary is type of list which let's you store arguents ``` user = {'username': None, 'password-hash': None, 'salt': None}``` and then use them or edit them by using name of the element instead of the number ``` user['username'] = username user['password-hash'] = key user['salt'] = salt ```. Register and log in are similar processes. In both we ask user to enter username and password. In registration we store username and password. We encrypt password using salt and hashlib library. Fisrt we generate salt ``` salt = os.urandom(32) ```. That is 32 random numbers that we will add to passsowrd eneter by user to make it harder to decrypt. Than we generate log in key by encriptyng the passowrd ```key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)```. Number 1000 at the end means that we run algorithm 1000 times. For log in we take password that user enters, repat process from before (add salt and encrpyt everything together) and then we compare what we generated to stored key. This is not finnished login system yet. Program will be further developed and flow digagram above will be updated accordingly. This is just outline / simple base for actuall login. Program for now stores data just in program meaning when we stop it data is lost. we also don't have actual login part of the program yet. User is not able to enter user name in passowrd to log in. For now this is done in program just for testing purposes.

## Showing dialog windows and opening them with buttons
I gave all the buttons in main app window, functionality to open related dialog windows. There are few steps in process of making this work:
1. We create class for every window in our application. We do that by using syntax
```.py
class LoginApp(loginW):
    def __init__(self, parent=None):
        super(LoginApp, self).__init__(parent)
        self.setupUi(self)
 ```
 LoginApp class I created, is inheriting from LoginWindow class. I created UI in QTdesigner, then I used ```pyuic5 file.ui -o file.py ``` comand to convert it to py file. This is where loginWindow class is coming from. It has all visual properties of my window. The method ``` def __init__``` is used to initialize the window and set it up with ``` self.setupUi(self) ``` command. The only exception to this process is MainWindow which is also inheriting from QMainWindow class: ``` class MainWindowApp(QMainWindow, mainW): ```. Everything else is the same.
2. To open dialog window I create methods under MainWindowApp class.
```.py 
    def addFunc(self):
        addVar = AddApp(self)
        addVar.show()
```
AddApp is class of the window we are opening.
3. We can connect each button to specific method. We do that by using the line
```.py
self.name_of_button.clicked.connect(self.nameOfMethod)
```
