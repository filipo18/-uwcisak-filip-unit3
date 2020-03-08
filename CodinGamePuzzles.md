Codin Game Puzzles
=======================

## Onboarding
```.py
# game loop
while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Write an action using print

    if dist_1 < dist_2:
        print(enemy_1)
    else:
        print(enemy_2)
```

## Descent
This problem was driving me crazy. It seemed soo simple but yet I didn't understood why my code is not working. I find it hard to understan what are input, what are ouptputs and in what way all this gets delivered into the code. My pgorgram started working when I moved print function out of the loop which doesnt make sense to me. The way I undesrtood the question I should shoot the mountain every round not at the end of everything so I don't know how program is working.
```.py
while True:
    height = []
    for i in range(8):
        height.append(int(input()))
    print(height.index(max(height)))
```

## Thor
I got that one preatty quick. You just need to visualize letters given as numbers (+ 1 and - 1). I am supper proud of my 4-if sentance solution instead of using 8 if sentances.
```.py
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    move=""
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if light_y > initial_ty:
        move = "S"
        initial_ty +=1
    elif light_y < initial_ty:
        move = "N"
        initial_ty -=1
    if light_x > initial_tx:
        move += "E"
        initial_tx += 1
    elif light_x < initial_tx:
        move += "W"
        initial_tx -= 1

    print(move)
```
    
## There is no spoon
The amount of time I spend on this problem was no fun. Fisrt of all understanding theese problems as I already mentioned is always the hardest part. I don't like this concept of problems at all. When I figured out what game wants from me I figgured out most of the program preaty quick but it was not working and I couldn find a solution. After spending over an hour on this problem I decided to finnish it next day. I talked to classmates about this problem and today I finished it preaty quick.
import sys
import math

```.py
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

lines = []
for i in range(height):
    lines.append(input())  # width characters, each either 0 or .

#print(lines)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for line in range(height): # Vertical line index
    for node in range(width): # Horizontal position index
        
        x2 = -1
        y2 = -1
        
        x3 = -1
        y3 = -1
        

        if lines[line][node] == "0":
            x1 = node
            y1 = line
            
            for i in range(node+1, width):
                if lines[line][i] == "0":
                    x2 = i
                    y2 = line
                    break
                
            for i in range(line+1, height):
                if lines[i][node] == "0":
                    x3 = node
                    y3 = i
                    break
                    

            print(x1, y1, x2, y2, x3, y3)
```
