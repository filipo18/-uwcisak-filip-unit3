#This program will calculate time between 2 time stamps
hour1 = int(input())
min1 = int(input())
sec1 = int(input())

hour2 = int(input())
min2 = int(input())
sec2 = int(input())

total1 = (hour1 * 3600) + (min1 * 60) + sec1
total2 = (hour2 * 3600) + (min2 * 60) + sec2
print(total2 - total1)