---
title: "Chapter 7"
weight: 70
---

# Chapter 7 Exercise Solutions

[Download Solutions](../files/Ch_7.py)

Embedded solutions:
```python
# Exercises for Chapter 7 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)
import time

# 7.1
class Rectangle:

    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    
    # Don't name functions like this at home kids
    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

rect_1 = Rectangle(4, 40)
rect_2 = Rectangle(3.5, 35.7)
print("Rectangle 1 --- Width: " + str(rect_1.width) + " Height: " +
        str(rect_1.height) + " Area: " + format(rect_1.getArea(), ".3f") + 
        " Permieter: " + format(rect_1.getPerimeter(), ".3f"))
print("Rectangle 2 --- Width: " + str(rect_2.width) + " Height: " +
        str(rect_2.height) + " Area: " + format(rect_2.getArea(), ".3f") + 
        " Permieter: " + format(rect_2.getPerimeter(), ".3f"))

# 7.2 - Opinion -- Clashes with Python ideology:
# Why make these variables private if you're letting people modify them?!?!!?
# The whole point of __ a variable means "DONT TOUCH"
class Stock:

    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def __get_name__(self):
        return self.__name

    def __get_symbol__(self):
        return self.__symbol

    def __get_prev_price__(self):
        return self.__previousClosingPrice

    def __get_curr_price__(self):
        return self.__currentPrice

    def __set_prev_price__(self, previousClosingPrice):
        return self.__previousClosingPrice

    def __set_curr_price__(self, currentPrice):
        return self.__currentPrice

    def getChangePercent(self):
        return ((self.__currentPrice - self.__previousClosingPrice) 
                / self.__previousClosingPrice) * 100

stock_1 = Stock("INTC", "Intel Corporation", 20.5, 20.35)
print("Prince change of", stock_1.__get_name__() + ":", 
        stock_1.getChangePercent())

# 7.4 - Don't. Do. This. In. Python.
class Fan:

    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, radius = 5,
                    on = False, color = "blue"):
        self.__speed = speed
        self.__radius = radius
        self.__on = on
        self.__color = color

    def __get_speed__(self):
        return self.__speed

    def __get_radius__(self):
        return self.__radius

    def __get_on__(self):
        return self.__on

    def __get_color__(self):
        return self.__color

    def __set_speed__(self, speed):
        self.__speed = speed

    def __set_radius__(self, radius):
        self.__radius = radius

    def __set_on__(self, on):
        self.__on = on

    def __set_speed__(self, color):
        self.__color = color

fan_1 = Fan(Fan.FAST, 10, True, "yellow")
fan_2 = Fan(Fan.MEDIUM, 5, False, "blue")
print("Fan 1 --- Speed: " + str(fan_1.__get_speed__())
        + " Radius: " + str(fan_1.__get_radius__())
        + " Color: " + str(fan_1.__get_color__())
        + " On: " + str(fan_1.__get_on__()))
print("Fan 2 --- Speed: " + str(fan_2.__get_speed__())
        + " Radius: " + str(fan_2.__get_radius__())
        + " Color: " + str(fan_2.__get_color__())
        + " On: " + str(fan_2.__get_on__()))

# 7.8
class StopWatch:

    def __init__(self):
        self.__startTime = time.time()

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__stopTime = time.time()

    def getElapsedTime(self):
        return (self.__stopTime - self.__startTime) * 1000

watch = StopWatch()
sum = 0
watch.start()
for i in range(1, 1_000_000):
    sum += i
watch.stop()
print("Time of execution:", format(watch.getElapsedTime(), ".2f"), "ms")
```