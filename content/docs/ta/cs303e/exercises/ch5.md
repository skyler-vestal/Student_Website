---
title: "Chapter 5"
weight: 50
---

# Chapter 5 Exercise Solutions

[Download Solutions](../files/Ch_5.py)

Embedded solutions:
```python
# Exercises for Chapter 5 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)
import math

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
print("Tutition cost 10 years from now (ouch): $" 
        + format(value, ".2f"))
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

# 5.18
# BUCKLE IN!!! This one is hard =(
# Also don't comment like this at home.
# Just want to go through my thought process here.
fact_num = eval(input("Give me an integer: "))
# Start with 2 since every number is divisible by 1
div = 2
print_str = ""
# As long as we still have factors left to divide out
while fact_num > 1:
    # Check if this number is divisble in the first place
    if fact_num % div == 0:
        # Assume the number is prime
        div_is_prime = True
        # Check to see if it's not prime for numbers > 3
        if not (div == 2 or div == 3):
            # Check every possible factor > 1 
            # to see if the number is divisble
            for num in range(2, int(math.sqrt(div) + 1)):
                if div % num == 0:
                    # If a number is divisble we know 
                    # it's not prime. stop
                    div_is_prime = False
                    break
        # If the number is prime see how many times you can divide
        if div_is_prime:
            while fact_num % div == 0:
                # Reduce the number to get the remaining factors
                fact_num /= div
                # Append the number to the list. If it's not the last
                # number add a comma as well
                print_str += str(div) 
                if fact_num > 1:
                    print_str += ", "
    # Check the next number
    div += 1
print(print_str)

# 5.19
max_num = eval(input("Enter the number of lines: "))
# Make n layers
for layer in range(1, max_num + 1):
    layer_str = ""
    # Get some spacing that gets smaller for each layer from the left
    # Each number and the spaces after is 3 wide so 3 * layer makes sense
    edge_spacing = 45 - (3 * layer)
    for i in range(edge_spacing):
        layer_str += " "
    # Add the first number (fence-post problem)
    layer_str += str(layer)
    # For every number less than the first > 0 add it to the pyramid
    tmp_num = layer - 1
    while tmp_num > 0:
        # Adjust spacing based on if double-digit
        str_add = "  " if tmp_num < 9 else " "
        layer_str += str_add + str(tmp_num)
        tmp_num -= 1
    # Add the opposite way back up
    tmp_num = 2
    while tmp_num <= layer:
        str_add = "  " if tmp_num < 10 else " "
        layer_str += str_add + str(tmp_num)
        tmp_num += 1        
    print(layer_str)

# 5.21
for layer in range(8):
    layer_str = ""
    # Each space and numbers before it take 4 spaces total
    edge_spacing = 60 - (4 * layer)
    for i in range(edge_spacing // 2):
        layer_str += "  "
    # 1 is always first
    layer_str += "1"
    # Each power of 2 > 1 less than 2^layer
    for num in range(1, layer + 1):
        num_sq = 2 ** num
        # For each digit take away a space
        if num_sq < 10:
            sp_width = "   "
        elif num_sq < 100:
            sp_width = "  "
        else:
            sp_width = " "
        layer_str += sp_width + str(num_sq)
    num = layer - 1
    # Count down powers of 2 to 1
    while num >= 0:
        # For each digit take away a space
        num_sq = 2 ** num
        if num_sq < 10:
            sp_width = "   "
        elif num_sq < 100:
            sp_width = "  "
        else:
            sp_width = " "
        layer_str += sp_width + str(num_sq)
        num -= 1
    print(layer_str)
```