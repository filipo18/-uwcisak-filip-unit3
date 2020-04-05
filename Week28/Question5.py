# This program will Write a Python program to calculate a dog's age in dog's years
# What is meant by "go to the editor" instruction

age = int(input("What is the dog's age in dog's years? "))
hYears = 0

if age == 1:
    hYears = 10.5
elif age == 2:
    hYears = 21
else:
    hYears = 21 + 4*(age-2)

print(hYears)