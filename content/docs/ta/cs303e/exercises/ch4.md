---
title: "Chapter 4"
weight: 40
---

# Chapter 4 Exercise Solutions

[Download Solutions](../files/Ch_4.py)

Embedded solutions:
```python
# Exercies for Chapter 4 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)

import math
import random

# 4.1
a, b, c = eval(input("Enter, a, b, c: "))
discrim = b ** 2 - (4 * a * c)
if discrim < 0:
    print("The equation has no real roots")
else:
    root_1 = (-b + math.sqrt(discrim)) / (2 * a)
    if discrim == 0:
        print("The root is", root_1)
    else:
        root_2 = (-b - math.sqrt(discrim)) / (2 * a)
        print("The roots are", root_1, "and", root_2)

# 4.2
num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)
num_3 = random.randint(0, 9)
add_string = str(num_1) + " + " + str(num_2) + " + " + str(num_3)
answer = eval(input("What is " + add_string + "? "))
print(add_string, "=", answer, "is", answer == num_1 + num_2 + num_3)

# 4.4
num_1 = random.randint(0, 99)
num_2 = random.randint(0, 99)
add_string = str(num_1) + " + " + str(num_2)
answer = eval(input("What is " + add_string + "? "))
print(add_string, "=", answer, "is", answer == num_1 + num_2)

# 4.6
weight = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))
inches += feet * 12

KILOGRAMS_PER_POUND = .45359237
METERS_PER_INCH = .0254
weight_in_kilograms = weight * KILOGRAMS_PER_POUND
height_in_meters = inches * METERS_PER_INCH
bmi = weight_in_kilograms / (height_in_meters ** 2)

print("BMI is", bmi)
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")

# 4.8
num_1, num_2, num_3 = eval(input("Enter 3 numberss (a, b, c): "))
if num_1 > num_2:
    num_1, num_2 = num_2, num_1
if num_2 > num_3:
    num_2, num_3 = num_3, num_2
if num_1 > num_3:
    num_1, num_3 = num_3, num_1
if num_1 > num_2:
    num_1, num_2 = num_2, num_1

print("Numbers ordered:", num_1, num_2, num_3)

# 4.10
num_1 = random.randint(0, 99)
num_2 = random.randint(0, 99)
mult_string = str(num_1) +  " * " + str(num_2)
real_answer = num_1 * num_2
answer = eval(input("What is " + mult_string + "? "))
if real_answer == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", mult_string, "is", real_answer)

# 4.11
# Omitted due to similarity with assignment 4/5

# 4.14
flip = random.randint(0, 1)
guess = input("Guess heads or tails: ")
guess_num = 0 if guess == "heads" else 1
if flip == guess_num:
    print("Correct!")
else:
    print("Wrong guess.")

# 4.17
user_move = eval(input("scissor (0), rock (1), paper (2): "))
computer_move = random.randint(0, 2)

user_display = "scissor"
if user_move == 1:
    user_display = "rock"
elif user_move == 2:
    user_display = "paper"

computer_display = "scissor"
if computer_move == 1:
    user_display = "rock"
elif computer_move == 2:
    user_display = "paper"

outcome = user_move - computer_move
if outcome == 0:
    print("The computer is " + str(computer_display) + ". You are "
            + str(user_display) + " too. It is a draw.")
else:
    result = "You won." if outcome == 1 else "You lost."
    print("The computer is " + str(computer_display) + ". You are "
            + str(user_display) + ". " + result)

# 4.22
x, y = eval(input("Enter a point with two coordinates: "))
dist = math.sqrt(x ** 2 + y ** 2)
result = "is"
if dist > 10:
    result += " not"
print("Point (" + str(x) + ", " + str(y) + ") " + result + " in the circle")
```