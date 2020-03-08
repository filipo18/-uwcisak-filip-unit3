Codin Game Puzzles
=======================

## Onboarding



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
```
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
    
