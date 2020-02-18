# This program will Graph the equation for the wave function
# cos(x) in the range x = [-10, 10] with steps of 0.5
import math
import numpy
import matplotlib.pyplot as pyplot

a = [n for n in numpy.arange(-10, 10, 0.5)]
b = [math.cos(n * 0.5) for n in a]

# Create graph
pyplot.plot(a, b)
# Title for axis
pyplot.xlabel('x')
pyplot.ylabel('$Y = cos(x)$')
# Show graph
pyplot.show()