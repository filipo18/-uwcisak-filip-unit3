# Demonstration of reduce function
from functools import reduce


# Multiply all the numbers in a list
data = [2, 3, 7, 11, 13, 17, 19, 23, 29]
multipier = lambda x, y: x*y
print(reduce(multipier, data))

product = 1
for x in data:
    product = product * x
print(product)

