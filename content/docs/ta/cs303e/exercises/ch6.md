---
title: "Chapter 6"
weight: 60
---

# Chapter 6 Exercise Solutions

[Download Solutions](../files/Ch_6.py)

Embedded solutions:
```python
# Exercises for Chapter 6 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)

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
```