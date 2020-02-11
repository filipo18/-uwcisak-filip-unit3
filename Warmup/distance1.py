# This program will calculate distance from city 1 to cities 2 3 and 4
import mylib
# Define cities location
cities = [(3, 5), (9, 10), (7, 8), (15, 7)]
names = ['A', 'B', 'C', 'D']


for i in range(4):
    cityA = cities[i]
    for i_2 in range(i+1, 4):
        cityB = cities[i_2]
        d = mylib.distance(origin=cityA, target=cityB)
        print('Distance between city {} and {} is {}'.format(names[i], names[i_2], d))