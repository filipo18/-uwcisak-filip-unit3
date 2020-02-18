import random
import matplotlib.pyplot as pyplot

# Create list of numbers form 1 to 1000
x = [i for i in range(1, 1000)]

# Generate a random number from 1 to 100 1000 times
y = list()
for i in range(1, 1000):
    rand = random.randrange(1, 100, 1)
    y.append(rand)

print(x)
print(y)

# Create graph
pyplot.plot(x, y)
# Title for axis
pyplot.xlabel('x')
pyplot.ylabel('Y = Random 1 to 100')
# Show graph
pyplot.show()

# Calculate average of the 1000 random numbers
sum = 0
for i in y:
    sum = i + sum
print(f"Average of 1000 random numbers is {sum / 1000}")

