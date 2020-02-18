# Generate a random number from 1 to 100 1000 times
import random
num = list()
for i in range(1, 1000):
    rand = random.randrange(1, 1000, 1)
    num.append(rand)


# This program will put numbers defined in array in order
    # Looping through the numbers unitl they are in order
    for var in range(len(num)-1, 0, -1):
        for i in range(var):
            # if first number is bigger than second one make seocond number first and first second
            if num[i] > num[i+1]:
                temp = num[i]
                num[i] = num[i+1]
                num[i+1] = temp

print(num)
