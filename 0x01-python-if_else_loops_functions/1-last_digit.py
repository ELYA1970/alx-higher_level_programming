#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = 10
if number < 0:
    mod *= -1
o = number % mod
if number < 0:
    o = number % -10
if o > 5:
    print(f"Last digit of {number} is {o} and is greater than 5")
elif o < 6 and o != 0:
    print(f"Last digit of {number} is {o} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {o} and is 0")
