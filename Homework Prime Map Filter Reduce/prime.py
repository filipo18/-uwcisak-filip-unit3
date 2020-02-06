# Prime number video

# Function venison 1
import time
import math

# Return true if n is a prime number, if it's not return false
def prime_v1(n):
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def prime_v2(n):
    # Function versions 2, test all divisors from 2 to sqrt(n)
    if n == 1:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True


def prime_v3(n):
    # Function venison 3, if number is even it is not prime, if
    # it is odd than divide just with odd numbers
    if n == 1: # one is not prime
        return False
    # If it is even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    # we will check every number from 3 to sqrt(n) rounded down + 1, and count by to to
    # work only with odd numbers
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
        return True


# ==== Check time ====
t0 = time.time()
for n in range(1, 100000):
    prime_v3(n)
t1 = time.time()
print("Time required: ", t1 - t0)

