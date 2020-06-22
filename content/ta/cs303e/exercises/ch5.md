---
title: "Ch5"
date: 2020-06-22T13:55:56-05:00
draft: true
---

# Chapter 5 Exercise Solutions

Download the solution here

Embedded solutions:
```python
# Exercises for Chapter 4 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)

# 5.1
input_prompt = "Enter an integer, the input ends if it is 0: "
keep_running = eval(input(input_prompt)) != 0
while keep_running:
    keep_running = eval(input(input_prompt)) != 0

# 5.3
print("Kilograms    Pounds")
for kilos in range(1, 200):
    pounds = kilos * 2.2
    print(format(kilos, "<14") + format(pounds, "5.1f"))

# 5.9
value = 10000
INTEREST = .05
for i in range(10):
    value *= (1 + INTEREST)
print("Tutition cost 10 years from now (ouch): $" + format(value, ".2f"))
four_year_cost = value
for i in range(3):
    value *= (1 + INTEREST)
    four_year_cost += value
print("Tuition for 4 years starting 10 years from now (double ouch): $" + 
        format(four_year_cost, ".2f"))

# 5.14
n = 0
while n ** 2 <= 12000:
    n += 1
print(n, "is the smallest number that is less than 12,000")
```