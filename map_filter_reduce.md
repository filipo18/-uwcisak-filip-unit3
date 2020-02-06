Map, filter and reduce funtions
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
