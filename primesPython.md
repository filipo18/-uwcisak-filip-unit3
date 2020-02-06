Primers in Python
===================

Goal was to crate function that checks if number is prime or not. Based on [Video](#Citations) I created 3 diffrent functions.
# Version 1
Prime_v1 is simplest and shortest one of them. The first step will be the same for all functions. Number one is prime number but it slips out of all of our algorithms so we start with 
```.py
    if n == 1:
        return False
```
Second step is to divide number with all the numbers from 2 to n-1. If we use ```for d in range(2, n):``` python will loop from 2 to n - 1. To check if number is divisible we use ``` % ```. This gives us remainder of division and if reminder of any divison is 0, number is not prime. If algorithm loops though all the numbers and doesn't find one number that divides n, number is prime:
```.py
    if n % d == 0:
        return False
return True
```
Program is working but if we want to check big amount of numbers, that can take some time. To measure time, so we have comaparable quantity, we import time module and substract start time of operation from end time of operation. We will use that part of code to test every version of this program.
```.py
import time
t0 = time.time()
for n in range(1, 100000): # This is range in which we are searching for prime numbers
    prime_v1(n)
t1 = time.time()
print("Time required: ", t1 - t0) # We substract start time from end time
```










# Citations
“ Python and Prime Numbers || Python Tutorial || Learn Python Programming.” YouTube, YouTube, 28 June 2017, www.youtube.com/watch?v=2p3kwF04xcA&feature=youtu.be.
