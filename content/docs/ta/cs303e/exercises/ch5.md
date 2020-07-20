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
# Witheld due to similarity with assignment 11

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
    
# 5.23 - A little off since the sample output doesn't round
loan = eval(input("Loan Amount: "))
years = eval(input("Number of Years: "))
print(format("Interest Rate", "<16"), format("Monthly Payment", "<16"),
        format("Total Payment", "<16"))
yearly_interest = .05
while yearly_interest < .08125:
    monthly_interest = yearly_interest / 12
    monthly_payment = (loan * monthly_interest / (1 - 
        1 / (1 + monthly_interest) ** (years * 12)))
    total_payment = monthly_payment * years * 12
    print(format(yearly_interest, "<16.3%"), format(monthly_payment, "<16.2f"),
            format(total_payment, "<16.2f"))
    yearly_interest += .00125

# 5.24
loan = eval(input("Loan Amount: "))
years = eval(input("Number of Years: "))
ann_interest = eval(input("Annual Interest Rate: "))

monthly_interest = ann_interest / 1200
monthly_payment = (loan * monthly_interest / (1 - 
         1 / (1 + monthly_interest) ** (years * 12)))
total_payment = monthly_interest * years * 12
print("\nMonthly Payment:", format(monthly_payment, ".2"))
print("Total Payment:", format(total_payment, ".2"))
print()

print(format("Payment #", "<10"), format("Interest", "<10"),
        format("Principal", "<10"), format("Balance", "<10"))
for i in range(1, 12 * years + 1):
    interest = monthly_interest * loan
    principal = monthly_payment - interest
    loan -= principal
    print(format(i, "<10.0f"), format(interest, "<10.2f"),
        format(principal, "<10.2f"), format(loan, "10.2f"))

# 5.25
sum_left = 0
sum_right = 0
n = 50_000
for i in range(1, n + 1):
    sum_left += 1 / i
    sum_right += 1 / abs(n - (i - 1))
print("Sum from left :", sum_left)
print("Sum from right:", sum_right)
print("Difference    :", abs(sum_left - sum_right))

# 5.28
item = 1
e = 1
for i in range(1, 1_000_000 + 1):
    item = item / i
    e += item
    # Added i < 20 since it's the same
    if i % 10_000 == 0 or i < 20:
        print("e for", i, "iterations is:", format(e, ".51"))

# 5.29
count = 0
curr_line = ""
for year in range(2001, 2100 + 1):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        count += 1
        curr_line += str(year) + " "
        if count == 10:
            print(curr_line)
            count = 0
            curr_line = ""

# 5.35
perfect_nums = ""
for num in range(2, 10_000):
    div_sum = 1
    for div_num in range(2, num):
        if num % div_num == 0:
            div_sum += div_num
    if num == div_sum:
        perfect_nums += str(num) + " "
print("Perfect Numbers:", perfect_nums)

# 5.45
num = eval(input("Enter a decimal integer: "))
hex_num = ""
while num > 0:
    div_digit = num % 16
    num //= 16
    if div_digit < 10:
        div_digit = str(div_digit)
    elif div_digit == 10:
        div_digit = "A"
    elif div_digit == 11:
        div_digit = "B"
    elif div_digit == 12:
        div_digit = "C"
    elif div_digit == 13:
        div_digit = "D"
    elif div_digit == 14:
        div_digit = "E"
    else:
        div_digit = "F"
    hex_num = div_digit + hex_num
print("Hexadecimal equivelant:", hex_num)
```