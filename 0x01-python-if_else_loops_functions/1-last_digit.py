#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
    num = number % 10
    num = -num
    number = -number
else:
    num = number % 10
if num > 5:
    a = "is greater than 5"
elif num != 0 and num < 6:
    a = "is less than 6 and not 0"
else:
    a = "is 0"
print(f"Last digit of {number} is {num} and {a}")
