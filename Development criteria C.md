Development 
============

# Registration

![Registration flow diagram](Login.jpg)

**Fig 1.** Registration flow diagram

This is ethod for secure log in where developer is not able to see password user has entered. We achive that by using ``` hashlib ``` and ```os``` librarys. Fisrt step in the flow diagram Fig 1. is to crate dictionary. Dictionary is type of list which let's you store arguents ``` user = {'username': None, 'password-hash': None, 'salt': None}``` and then use them or edit them by using name of the element instead of the number ``` user['username'] = username user['password-hash'] = key user['salt'] = salt ```. Register and log in are similar processes. In both we ask user to enter username and password. In registration we store username and password. We encrypt password using salt and hashlib library. Fisrt we generate salt ``` salt = os.urandom(32) ```. That is 32 random numbers that we will add to passsowrd eneter by user to make it harder to decrypt. Than we generate log in key by encriptyng the passowrd ```key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)```. Number 1000 at the end means that we run algorithm 1000 times. For log in we take password that user enters, repat process from before (add salt and encrpyt everything together) and then we compare what we generated to stored key. This is not finnished login system yet. Program will be further developed and flow digagram above will be updated accordingly. This is just outline / simple base for actuall login. Program for now stores data just in program meaning when we stop it data is lost. we also don't have actual login part of the program yet. User is not able to enter user name in passowrd to log in. For now this is done in program just for testing purposes.

# Design
Picture below shows how GUI of program will eventually look. Even though this is not compleatly final version, it is preatty close to how final version will look.

![GUI design](GUIdesign.png)

**Fig 2.** GUI design

When user enters his credentials home page opens. TAble of guitars is shown there. Buttons open dialog boxes for adding, removing, editing, lending and returning guitar.
