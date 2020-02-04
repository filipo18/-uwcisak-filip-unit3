#This program Print its tens digit
num = int(input())
ones = num % 10
tens = num % 100
print((tens - ones) / 10)