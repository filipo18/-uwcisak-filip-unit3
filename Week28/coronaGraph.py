import matplotlib.pyplot as plt
import csv


with open('total_cases.csv') as dt:  # Open csv file
    # Set the lists and variable
    dataWorld = []
    dataSlovenia = []
    dataItaly = []
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
        
            # list of cases for slovenia
            if row[135] == "":  # if there is no new cases we need to add 0 to the list so we have data
                dataSlovenia.append(int(0))
            else:
                dataSlovenia.append(int(row[135]))
            
            # First I though my program is not working but then I tried to plot Italy and it turns out its working
            # The reason why line for slovenia looks straight is because we have 258 cases and this number is
            # Irrelevant for total number of cases in the world
            if row[77] == "": 
                dataItaly.append(int(0))
            else:
                dataItaly.append(int(row[77]))


# Plot the graph and name the axes
plt.plot(dayNum, dataWorld, dayNum, dataSlovenia, dayNum, dataItaly)
plt.xlabel('Day')
plt.ylabel('Cases - BLUE: World, ORANGE: Slovenia, GREEN: Italy')
plt.show()
