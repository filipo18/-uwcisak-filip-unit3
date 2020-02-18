# This program will Graph the equation for the wave function
# 14*sin(0.5*x) in the range x = [-10, 10] with steps of 0.1.
import matplotlib.pyplot as pyplot
import math
import numpy


# Normal for loop does not allow us use decimals so we need to import numpy library
# and use arrange function
x = [i for i in numpy.arange(-10, 10, 0.1)]
y = [14*math.sin(0.5*i) for i in x]

# Create graph
pyplot.plot(x, y)
# Title for axis
pyplot.xlabel('x')
pyplot.ylabel('$Y = 14 * sin(o.5 * x)$')
# Show graph
pyplot.show()
print(x)
print(y)

