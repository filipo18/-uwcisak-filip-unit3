# Program will calculate who is the winner
import math

distanceB = 100
distanceC = 110
acc = 5
speed = 10

timeB = distanceB / speed
timeC = math.sqrt((distanceC * 2) / acc)

print(timeB)
print(timeC)
if timeB > timeC:
    print("Cheetah Winer")
else:
    print("Bolt Winner")