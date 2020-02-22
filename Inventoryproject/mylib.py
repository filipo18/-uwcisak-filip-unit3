# This is my library of very useful functions

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
