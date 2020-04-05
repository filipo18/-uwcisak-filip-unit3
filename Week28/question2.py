# This program will generate a dictionary that contains (i, i*i) such that i is an integral number between 1 and n (both included). The program should print the dictionary.

len = int(input("Choose the number n: "))
dict = {}

for i in range(1, len+1):
    dict[str(i)] = i*i # Dictionary assings values to strings so we need to convert i to a 'string'

print(dict)