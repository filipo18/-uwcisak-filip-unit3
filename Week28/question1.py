# This program will accept a string and calculate the number of digits and letters. 

text = input("Please input a string: ")

let = 0
num = 0

for i in text:
    if i.isalpha(): # Checks if i is letter
        let += 1
    elif i.isdigit(): # Checks if i is digit
        numb += 1 

print(f"Letters: {letters}, Numbers: {numbersn}")
