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
Version 1 takes 83.89s to find primes in range from 1 to 100,000.

# Version 2
If we look at factors of few numbers, we notice that after values croos square root of a number, we are not getting any new factors. We can use this property to our advetage to lower number of divisions we do. The part of program that is testing divison works perfectly and we can't make it better so we will not change it:
```-py
    if n % d == 0:
     return False
return True
```
To get max divisor to set up a range Python has a math modul ``` import math ``` To decide a renge of divisors we round down square root of our n number ``` max_divisor = math.floor(math.sqrt(n)) ```. To tst every posible divisor we add 1 to that number and set up a range:
```.py
for d in range(2, 1 + max_divisor):
```
This verion of the program is much faster. Time we get for numbers in range 1 to 100,000 is 0.31s.

# Version 3
There is a way to make number of divisions we try even smaller. It is no point in testing even numbers because they are not prime, except for 2 so first we deal with all even numbers and 2 ( 2 is a prime numeber):
```.py
    if n > 2 and n % 2 == 0:
        return False
```
Now we don't have 1, 2 and all the even numbers any more. So use use same proces from before for max divisor, we set up range from 3 to max_divisor + 1, but his time we count up from 3 by 2. In that way we are testing only odd numbers. To count by bigger steps than 1 in python you just add third element in range bracket seperated by coma:
```.py
for d in range(3, 1 + max_divisor, 2):
```
Version 3 is the fastest one of all version. It checked numbers from 1 to 100,000 in 0.06s




# Citations
“ Python and Prime Numbers || Python Tutorial || Learn Python Programming.” YouTube, YouTube, 28 June 2017, www.youtube.com/watch?v=2p3kwF04xcA&feature=youtu.be.
