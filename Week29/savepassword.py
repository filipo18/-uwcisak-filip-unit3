# This program asks user for his first name and last name and number (1,100) and then
# outputs his email num times in output.txt file that is in the same folder as the program

# First I collect inputs from the user
name = input("Enter your name:")
lastname = input("Enter your last name:")
num = int(input("Enter number between 1 and 100:"))
text_file = open("output.txt", "w") # open text file in write mode

# Checking the number entered
if 1 < num < 101:
    # writing emails to the text file
    for i in range(1, num + 1):
        text_file.write(f"{name}.{lastname}{i}@uwcisak.jp\n")
else:
    print('Input error, please try again')

text_file.close() # close text file
