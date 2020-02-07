Map, filter, reduce, tuple and lambda funtions
====================================

# Map
Map function is a way to apply function to each piece of data. In our example we have aray of radiis and we want to caluculate area of the circle. First we define funstion ``` def area(r) ``` and list of data ``` radii = [2, 5, 7.1, 0.3, 10] ```. With the map function you first specifiy the function then you specify the data to iterate over:
```.py
map(area, radii)
```
If we want to present map in a list we use list comand ``` list(map(area, radii)) ```. My question on this point is what can we do or how do we use map if we don't change it to lsit?

To operate with a touples ```temps = [("Berlin" 29), ("Cairo", 36)...]``` you can use ``` lambda data: ``` to crate a function:
```.py
function = labmda data: (data[position in tuple starting 0], data[1])
```
```Data []``` in brackets will behave as normal variable.


# Filter

Filer function is used to filter out the data we don't need. Fist argument is function we want to use, second argument is the list of data ``` filter(function, data) ``` The filter function will only return the data for which the function is ```TRUE```. To use this in example we will show the numbers from the array that are bigger than average of the array:
```.py
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
```
To caluclate the average we first need to import statistics module ``` import statistics ```. We calculate the average ``` avg = statistics.mean(data)```  and take it to the filter function where we create small function in one line using lambda:
```.py
print(list(filter(lambda x: x > avg, data)))
```
*note: lambda is way to define short function in line, will be explained in detail bellow

We can also use filter function to filter out false data. In case of lists, false data is empy argument ``` " " ``` which is defined by ``` none ```. Here is example of filtering false data out of the list:


 



# Reduce

To get reduce function we need to import it ``` from functools import reduce ```. To use it we need to have defined data we want to use and function with two variables. If ``` Data = [a1, a2, a3, ...] ``` and function f(x,y) for example ``` x * y ```, the reduce funtion will take first two elements and multiply them ``` product1 = a1 * a2 ``` and then take value and add it to funcition with next element ``` product2 = product1 * a3 ```. Here is the example how to use it to multiply set of numbers:
```.py
data = [2, 3, 7, 11, 13, 17, 19, 23, 29]
multipier = lambda x, y: x*y
print(reduce(multipier, data))
```
*note: lambda is way to define short function in line, will be explained in detail bellow

Most of the times for loop can replace reduce funtion:
```.py
product = 1
for x in data:
    product = product * x
print(product)
```

