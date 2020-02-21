# This program will list all the elements with even index number

# Split returns a list of strings after breaking the given string by specified separator
a = input().split()
for i in range(0, len(a), 2):
  print(a[i])


# ########### Even elements ################
# This program will print even elements from the list

# Creates list of numbers from the input
a = [int(i) for i in input().split()]
for arg in a:
    # If number is divisible by 2 it's even
    if arg % 2 == 0:
    print(arg)

# ######## Greater than previous#########
# This program will print all the elements that are grater than previous

a = [int(i) for i in input().split()]
# We start loop from 1 because we can't compare first element to anything
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

# ########Neighbours of the same sign########
# This program will print out two adjacent elements if they are of same sign
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if (a[i] * a[i-1]) > 0:
        print(a[i], a[i-1])


# #######Greater than neighbours####
# This program will print number of  numbers that are greater from both of their neighbours
a = [int(i) for i in input().split()]
count = 0
# range excluding first and last number
for i in range(1, len(a) - 1):
  if a[i - 1] < a[i] > a[i + 1]:
    count += 1
print(count)
