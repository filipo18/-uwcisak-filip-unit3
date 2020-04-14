import matplotlib.pyplot as plt
import csv
import numpy
import scipy.stats


with open('total_cases.csv') as dt:  # Open csv file
    # Set the lists and variable
    dataWorld = []
    # I will count days with this variable and the list
    dayNum = []
    day = 0
    values = csv.reader(dt, delimiter=",")
    for row in values:
        if row[0] == 'date':  # First argument in every line is a date and we want to skip date, we want just numbers
            pass
        else:
            # create list of days to count them
            dayNum.append(day)
            day += 1

            # List of cases for the world
            dataWorld.append(int(row[1]))  # While debugging I found out I need to change data type of arguments to int

with open('gold_prices.csv') as dt2:
    dataGoldS = []
    values2 = csv.reader(dt2, delimiter=",")
    for row in values2:
        dataGoldS.append(row)
dataGoldF = [float(item) for item in dataGoldS[0]]  # Change list of strings to list of floates

# Here I calculate correlation coefficient
world = numpy.array(dataWorld)
gold = numpy.array(dataGoldF)
print(f"The correlation coefficient is {scipy.stats.pearsonr(world, gold)[0]}") # this functions

# Plot the graph and name the axes
plt.plot(dayNum, dataWorld, dataGoldF)
plt.xlabel('Day')
plt.ylabel('Cases - BLUE: World, ORANGE: Slovenia, GREEN: Italy')
plt.show()
