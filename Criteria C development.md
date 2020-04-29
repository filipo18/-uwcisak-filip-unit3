Development 
============
## Registration

![Registration flow diagram version 1.0](Login.jpg)

**Fig 1.** Registration flow diagram version 1.0

We created this in class just as an example how secure login can be created. The final version will be similar to this and will follow similar priciples. This is ethod for secure log in where developer is not able to see password user has entered. We achive that by using ``` hashlib ``` and ```os``` librarys. Fisrt step in the flow diagram Fig 1. is to crate dictionary. Dictionary is type of list which let's you store arguents ``` user = {'username': None, 'password-hash': None, 'salt': None}``` and then use them or edit them by using name of the element instead of the number ``` user['username'] = username user['password-hash'] = key user['salt'] = salt ```. Register and log in are similar processes. In both we ask user to enter username and password. In registration we store username and password. We encrypt password using salt and hashlib library. Fisrt we generate salt ``` salt = os.urandom(32) ```. That is 32 random numbers that we will add to passsowrd eneter by user to make it harder to decrypt. Than we generate log in key by encriptyng the passowrd ```key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)```. Number 1000 at the end means that we run algorithm 1000 times. For log in we take password that user enters, repat process from before (add salt and encrpyt everything together) and then we compare what we generated to stored key. This is not finnished login system yet. Program will be further developed and flow digagram above will be updated accordingly. This is just outline / simple base for actuall login. Program for now stores data just in program meaning when we stop it data is lost. we also don't have actual login part of the program yet. User is not able to enter user name in passowrd to log in. For now this is done in program just for testing purposes.

### Registration Version 2 (Decomposition)

For verison 2.0 we used 2 functions created by Alessandro Molina. [source](https://www.vitoshacademy.com/hashing-passwords-in-python/) **First function** ```def hash_password(password):``` takes password from the user and converts it into hash. TO make password more secure we need to create a salt like in version 1. 
```.py
salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
``` 
```os.urandom(60)``` Creates 60 random bytes of infrormation. ```.hexdigest()``` Adding this we get has of a default sze of 64 bytes.  To convert 64bytes into 64 ascii text characters we use ```.encode('ascii')``` Then we add salt to a password and hash it to defualt 64 bytes 100000 times to increase randomness:
```.py
pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
```
```password.encode('utf-8')``` Converts password enetered using UTF-8 protocol. To finnish the function we convert 64bytes of binary information to a hexadecimal string ```  pwdhash = binascii.hexlify(pwdhash)``` and return a string where salt is followed by the hashed password. ``` return (salt + pwdhash).decode('ascii')``` 
**Second function** ```def verify_password(stored_password, provided_password):``` takes password from the user, comapres it to hash we stored earlier and verifies if it's the same or not. First we take salt as the first 64 characters of the hash
```.py
salt = stored_password[:64]
```
Then we take password from the user as the second 64 characters of the hash. An then with that we generate the hash again following the same process as before and if that gives us same hash as we got from the fisrt function we return True:
```.py
pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
pwdhash = binascii.hexlify(pwdhash).decode('ascii')
return pwdhash == stored_password
```


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

## Showing data from .csv file in the table 
To show data from .csv file in the mainAplication table, we create method for showing data in the table. First step in this method is to open the file and set how values are separated. In our case wiht comma ```delimiter="," ```
```.py
        with open('name_of_the_file.csv') as whatever_you_want:
            file = csv.reader(whatever_you_want, delimiter=",")
```
Then we use 2 for loops and enumerate function to spread data in the data table sorted by columns and rows
```.py
            for i, row in enumerate(file):
                for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(col))
```
``` self.tableWidget.setItem(i, j, QTableWidgetItem(col)) ``` This line asings values to boxes in the table. ``` enumerate() ``` function sets numbers to our rows and columns.



