# This program will tell if rook can make a move
firstC = int(input())
firstR = int(input())
secondC = int(input())
secondR = int(input())

if firstC == secondC or firstR == secondR:
    print("YES")
else:
    print("NO")