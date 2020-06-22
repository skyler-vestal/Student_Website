---
title: "Chapter 2"
weight: 20
---

# Chapter 2 Exercise Solutions

[Download Solutions](../files/Ch_2.py)

Embedded solutions:
```python
# Exercies for Chapter 2 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)

# 2.1
celsius = eval(input("Enter a degree in Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(celsius, "Celsius is", fahrenheit, "Fahrenheit")

# 2.2
radius, length = eval(input("Enter area and volume: "))
area = radius * radius * 3.14
volume = area * length
print("The area is", area)
print("The volume is", volume)

# 2.3
feet = eval(input("Enter a value for feet: "))
meters = feet * .305
print(feet, "feet is", meters, "meters")

# 2.4
pounds = eval(input("Enter a value in pounds: "))
kilograms = pounds * .454
print(pounds, "pounds is", kilograms, "kilograms")

# 2.5
subtotal, gratuity_rate = eval(input("Enter the subtotal and a gratuity rate: "))
gratuity = subtotal * gratuity_rate/100
total = subtotal + gratuity
# Don't think rounding to n digits have been covered yet ... using it anyway
print("The gratuity is", round(gratuity, 2), "and the total is", round(total, 2))

# 2.6
total = 0
num = eval(input("Enter a number between 0 and 1000: "))
total += num % 10
num //= 10
total += num % 10
num //= 10
total += num % 10
num //= 10
total += num % 10
num //= 10
print("The sum of the digits is", total)

# 2.7
mins = eval(input("Enter the number of minutes: "))
total_days = mins // 60 // 24
years = total_days // 365
remainder_days = total_days % 365
print(mins, "minutes is approximately", years, "years and", remainder_days, "days")

# 2.9
fahrenheit = eval(input("Enter the temeprature in Fahrenheit between -58 and 41: "))
wind_speed = eval(input("Enter the wind speed in miles per hour: "))
# Adjust wind speed to v^.16
wind_speed **= .16
wind_chill = (35.74 + (0.6215 * fahrenheit) - 
                (35.75 * wind_speed) + (0.4275 * fahrenheit * wind_speed))
# Again the answer is rounded despite the textbook not covering rounding to n digits
print("The wind chill index is", round(wind_chill, 5))

# 2.10
speed, accel = eval(input("Enter speed and acceleration: "))
length = speed ** 2 / (2 * accel)
print("The minimum runway length for this airplane is", round(length, 3), "meters")

# 2.16
v_0, v_1, t = eval(input("Enter v0, v1, and t: "))
avg_accel = (v_1 - v_0)/t
print("The average acceleration is", round(avg_accel, 4))

# 2.22
years = eval(input("Enter the number of years: "))
population = 312032486 + ((years * 365 * 24 * 60 * 60 // 7)
        + (years * 365 * 24 * 60 * 60 // 45) 
        - (years * 365 * 24 * 60 * 60 // 13))
print("The population in", years, "years is", population)
```