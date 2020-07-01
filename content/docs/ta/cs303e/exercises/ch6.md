---
title: "Chapter 6"
weight: 50
---

# Chapter 6 Exercise Solutions

[Download Solutions](../files/Ch_6.py)

Embedded solutions:
```python
# Exercises for Chapter 6 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)
import random

# 6.1
# CS 311 exercise =) - Prove that for any n the pentagonal number
# is an integer
def getPentagonalNumber(n):
    return n * (3 * n - 1) // 2

for i in range(10):
    line_str = str(getPentagonalNumber(i * 10 + 1))
    for j in range(2, 11):
        line_str += ", " + str(getPentagonalNumber(i * 10 + j))
    print(line_str)

# 6.2
def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

sum = sumDigits(eval(input("Enter a number: ")))
print("The sum of the digits is", sum)

# 6.8
def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32

def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

c_temp = 40.0
f_temp = 120.0
print(format("Celsius", "<15"), format("Fahrenheit", "<10"),
        "   |    ", format("Fahrenheit", "<15"), 
        format("Celsius", "<10"), sep="")
print()
for i in range(10):
    f_conv = celsiusToFahrenheit(c_temp)
    c_conv = fahrenheitToCelsius(f_temp)
    print(format(c_temp, "<15.1f"), 
        format(f_conv, "<10.1f"), "   |   ", 
        format(f_temp, "<15.1f"),
        format(c_conv, "<10.1f"), sep = "")
    c_temp -= 1
    f_temp -= 10

# 6.13
sum_ser = 0
print(format("i", "14"), "m(i)")
for i in range(1, 21):
    sum_ser += i / (i + 1)
    print(format(i, "<12"), format(sum_ser, "7.4f"))

# 6.14
sum_ser = 0
print(format("i", "14"), "m(i)")
for i in range(1, 902):
    sum_ser += 4 * (((-1) ** (i + 1)) / (2 * i - 1))
    if (i - 1) % 100 == 0:
        print(format(i, "<12"), format(sum_ser, "7.4f"))

# 6.18
n = eval(input("Enter n: "))
for row in range(n):
    line_str = ""
    for col in range(n):
        line_str += str(random.randint(0, 1)) + " "
    print(line_str)

# 6.19 - This one has really weird instructions for functions
# Don't name your methods like this at home kids:
# Also don't have three different functions for this ...
def leftOfTheLine(x_0, y_0, x_1, y_1, x_2, y_2):
    return point_calculation(x_0, y_0, x_1, y_1, x_2, y_2) > 0

def onTheSameLine(x_0, y_0, x_1, y_1, x_2, y_2):
    return point_calculation(x_0, y_0, x_1, y_1, x_2, y_2) == 0

# Another textbook mistake here :/
def rightOfTheLine(x_0, y_0, x_1, y_1, x_2, y_2):
    return point_calculation(x_0, y_0, x_1, y_1, x_2, y_2) < 0

# Making this to make things easier
def point_calculation(x_0, y_0, x_1, y_1, x_2, y_2):
    return (x_1 - x_0) * (y_2 - y_0) - (x_2 - x_0) * (y_1 - y_0)

x_0, y_0, x_1, y_1, x_2, y_2 = eval(input("Enter " +
    "coordinates for the three points p0, p1, and p2: "))

# You only need two if statements here ...
result = ""
if leftOfTheLine(x_0, y_0, x_1, y_1, x_2, y_2):
    result = "left side of the line"
elif rightOfTheLine(x_0, y_0, x_1, y_1, x_2, y_2):
    result = "right side of the line"
elif point_calculation(x_0, y_0, x_1, y_1, x_2, y_2):
    result = "same line from"
print("p2 is on the", result, "from p0 to p1")

# Better solution only needing 1 function o-o:
# result = "same line from"
# if point_calculation(x_0, y_0, x_1, y_1, x_2, y_2) > 0:
#     result = "left side of the line"
# elif point_calculation(x_0, y_0, x_1, y_1, x_2, y_2) < 0:
#     result = "right side of the line"
# print("p2 is on the", result, "from p0 to p1")

# 6.21
def sqrt(n):
    lastGuess = 1.01
    nextGuess = 1
    while abs(nextGuess - lastGuess) > 0.0001:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2
    return nextGuess

num = eval(input("Enter a number: "))
print("Sqrt:", sqrt(num))

# 6.28
# Withheld due to similarity with assignment 6
```