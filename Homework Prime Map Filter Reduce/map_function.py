# demonstration of map function
import math


def area(r):
    # Area of the circle with radius r
    return math.pi * (r**2)


radii = [2, 5, 7.1, 0.3, 10]

# method 1: Direct method
areas = []
for r in radii:
    a = area(r)
    areas.append(a)


# Method 2: use 'map' function
map(area, radii)  # map function will loop through list and plug values in the chosen function
areas = list(map(area, radii))
print(areas)