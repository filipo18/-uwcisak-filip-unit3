# This program will put numbers defined in array in order

# Define the array
num = [3, 4, 1, 100, 34, 17, 21, 16]
# Set the variable that will check if program is complete or not
check = 0
# measure length of the array
n = len(num)

# looping through the program until numbers are in order
while check < 8:
    # set to numbers in pairs as left and right variable that will be compared
    for val in range(n - 1):
        left = num[val]
        right = num[val + 1]
        # if first number is smaller than next one move to checking next 2 numbers
        if left < right:
            check += 1
        # if fist number is bigger than next one switch them
        elif left > right:
            num[val] = right
            num[val+1] = left
            # Print every step to the user
            print(*num, sep = ", ")
