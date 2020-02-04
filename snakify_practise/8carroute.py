#This program calucaltes how many days it take to cover rount of x lenght
km = int(input())
day = int(input())

if day % km == 0:
    print(day / km)
    
else:
    print((day // km) + 1  )
