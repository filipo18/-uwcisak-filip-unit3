# Security program
import hashlib
import os
import mylib

user = {'username': None, 'password-hash': None, 'salt': None}

print("1- Register")
print("2 - Log In")
print("3 - Exit")

opt = 10
while opt > 3:
    opt = int(input("Enter option (1, 2, or 3)"))

# User entered #1 Registration
username = input("Enter your username: ")
confirmed = False
while not confirmed:
    password = input("Enter your password: ")
    password_test = input("Confirm your password: ")
    if password == password_test:
        confirmed = True
print("done")
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
import binascii
user['username'] = username
user['password-hash'] = key
user['salt'] = salt
password_entered = "12345"
key_check = hashlib.pbkdf2_hmac('sha256', password_entered.encode('utf-8'), salt, 1000)
if key == key_check:
    print("Login Okay")
else:
    print("Login invalid")