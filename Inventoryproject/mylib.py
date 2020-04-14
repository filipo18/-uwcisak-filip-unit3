# This is my library of very useful functions
import hashlib
import binascii
import os

def me():
    print("Developer:".rjust(20), "Filip Ignijic")
    print("Date:".rjust(20), "5 Feb 2020")


def prime(x):
    # This function check if the number x is prime
    # Divide x by all the numbers from 2 to the x - 1
    # if the residuals of division are all different of zero then x is a prime
    for dev in range(2, x // 2):
        if x % dev == 0:
            return False
    return True


def distance(target, origin=(0, 0)):
    # This function calculates the pythagorean distance
    import math
    d = math.sqrt((target[0] - origin[0]) ** 2 + (target[1] - origin[1]) ** 2)
    return d


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:-1]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password