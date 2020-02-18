# This program will graph 1000 random numbers
import matplotlib.pyplot as pyplot

# Pythonic way
x = [i for i in range(-10, 10)]
y = [i**2 for i in x]

# Normal way with for loops
a = list()
for m in range(-10, 10):
    a.append(m)
b = list()
for n in a:
    b.append(n**2)

print(x)
print(a)
print(y)
print(b)

# Create graph
pyplot.plot(x, y)

# Title for axis
pyplot.xlabel('x')
pyplot.ylabel('$y = x^2$')

# Show graph
pyplot.show()