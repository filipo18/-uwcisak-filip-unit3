# This program will generate as many passwords as user wants
import random
import string

num = int(input("Enter how many passwords you want to generate:"))
for i in range(0, num):
    password = string.ascii_letters + string.digits + string.punctuation # combining letters digits and symbols
    print(''.join(random.choice(password) for i in range(20)))  # joining chosen characters 20 times
