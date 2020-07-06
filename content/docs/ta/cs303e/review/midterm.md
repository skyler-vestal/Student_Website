---
title: "Midterm"
weight: 10
---

![](/~ves314/img/study_2.gif?raw=true)

# Midterm Review

## Multiple Choice Section

The following is Mike's CS 312 Exam 1 from Fall 2019 and 2018. You can find the original page [here](https://www.cs.utexas.edu/~scottm/cs312/testStudyMaterials.htm). I've translated a few questions from Java to Python

### CS 312 Fall '19

1. What is output by the following code when it is run?
```python
x1 = 10
y1 = 2 + x1 // 3
x1 += 2
y1 -= 1
y1 = 3 + y1
print(x1, y1)
```
2. What is output by the following code when it is run?
```python
a2 = 2.0
b2 = 3.0
c2 = 2.0
b2 *= c2 * (a2 + b2)
print(b2, c2)
```
3. How many asterisks does the following code print out?
```python
for i in range(5):
    print("***")
    for j in range(3):
        print("*")
    print("***")
    for j in range(1, 6):
        print("*")
```
4. How many asterisks does the following code print out?
```python
for i in range(1, 11, 2):
    for j in range(i):
        print("*")
```
5. How many asteriks does the following code print out?
```python
def a():
    for i in range(1, 9):
        print("*")

def b():
    for i in range(3):
        print("*")
        a()
        print("*")

def c():
    a()
    b()
    for i in range(1, 4):
        a()
        b()

a()
b()
c()
```
6. What is output by the following code when it is run?
```python
def f(x6, y6):
    y6 -= 3
    x6 *= 2
    print(x6, y6)

x6 = -5
y6 = 5
f(x6, y6)
f(y6, x6)
print(x6, y6)
```
7. What is output by the following code when it is run?
```python
x5 = 2
y5 = 30
while y5 >= 4:
    x5 *= 2
    y5 = y5 / 2
print(x5, y5)
```
8. What is output by the following code when it is run?
```python
import math

a3 = -2.75
b3 = 3.751
c3 = -5.0
print(math.ceil(a3), math.floor(b3), math.ceil(c3))
```

### CS 312 Fall '18

1. What is output by the following code when it is run?
```python
x1 = 3
y1 = x1 * 3
a1 = x1 // 2 + y1 // 2
x1 = x1 + 2
y1 -= 1
a1 = a1 / 2
print(x1, y1, a1)
```
2. What is output by the following code when it is run?
```python
x2 = 1
y2 = 10
y2 *= 1 + x2 * (y2 - 12)
print(y2 - 10)
```
3. What is output by the following code when it is run?
```python
s3 = "x3"
x3 = 4
a3 = 2.0
print(x3, 2, s3, a3, 1, sep="")
```
4. How many asteriks does the following code print out?
```python
print("*")
for i in range(-1, 7):
    print("*")
    print("*")
print("*")
```
5. How many asteriks does the following code print out?
```python
for i in range(1, 6):
    print("**")
    for j in range(1, 11):
        print("**")
        print("***")
    print("*")
```
6. How many asteriks does the following code print out?
```python
for i in range(0, 5):
    for j in range(1, i + 1):
        print("*")
    for j in range(0, 4):
        print("*")
        for k in range(0, 4):
            print("*")
```
7. What is output by the following code when it is run?
```python
x7 = 6
y7 = 3
z7 = y7 * 10 % (x7 - (y7 * 2))
print(z7)
```
8. What is output by the following code when it is run?
```python
def function8(x, y):
    x += 1
    y -= 1
    print(x + y)
    
x8 = 8
y8 = -5
function8(y8, x8)
function8(x8, x8)
print(x8, y8)
``` 
9. What is output by the following code when it is run?
```python
def function9(x, y):
    x -= 1
    y *= 2
    return x + y

x9 = 5
y9 = 10
x9 = function9(x9, y9)
print(x9, y9)
```
10. What is output by the following code when it is run?
```python
def function10(x, y):
    x += 2
    y -= 2
    print(x * y)
    return x + y

x = 2
y = 3
print(function10(x, y) + x * y + function10(y, y))
```

## Written Section

### HackerRank Questions

The following are HackerRank programming questions to test your knowledge. To complete questions do the following:

1. Register an account
2. In the editor, change the language from Python 2 to Python 3:
![](/~ves314/img/hackerrank.png?raw=true)
3. Type your code within the `if __name__ == '__main__':` segment (you don't have to know why this if statement is here)
4. Write your code
5. Hit "Run Code" to test if your solution solves the sample input.
6. Hit "Submit Code" to test if your solution satisfies all test inputs.

On Target Problems:
* [Printing/Concatenation](https://www.hackerrank.com/challenges/whats-your-name/problem)
* [Using Functions](https://www.hackerrank.com/challenges/python-power-mod-power/problem)
* [If-Else](https://www.hackerrank.com/challenges/py-if-else/problem)
* [Loops](https://www.hackerrank.com/challenges/python-loops/problem)
* [Concatenaition/Loops](https://www.hackerrank.com/challenges/python-print/problem)
* [Functions](https://www.hackerrank.com/challenges/write-a-function/problem)

Difficult (Above Exam) Problems:
* [sWAP cASE](https://www.hackerrank.com/challenges/swap-case/problem)
    * Hint: `for let in s` will make `let` store each character in the string while iterating

## Solutions

### Multiple Choice
```
Fall '19:
1: 12 7
2: 30.0 2.0
3: 70
4: 25
5: 190
6:  -----
    -10 2
    10 -8
    -5 5
    -----
7: 16 3.75
8: -2 3 -5

Fall '18:
1: 5 8 2.5
2: -20
3: 42x32.01
4: 18
5: 265
6: 110
7: Error (Technically DivisionError) using % by 0
8:  -----
    3
    16
    8 -5
    -----
9: 24 10
10: -----
    4
    5
    17 
    -----
```

### Written Section
```python
########## HackerRank Questions ###########

##### On Target: #####

# Printing/Concatenation
def print_full_name(a, b):
    print("Hello", a, b + "! You just delved into python.")

# Using Functions
a = eval(input())
b = eval(input())
m = eval(input())
print(pow(a, b))
print(pow(a, b, m))

# If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n >= 20:
        print("Not Weird")

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)

# Print Function
if __name__ == '__main__':
    n = int(input())
    output = ""
    for i in range(1, n + 1):
        output += str(i)
    print(output)

# Functions
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


##### Difficult: #####

# sWAP cASE
def swap_case(s):
    new_str = ""
    for let in s:
        let_id = ord(let)
        if (let_id >= 65 and let_id <= 90 
                or let_id >= 97 and let_id <= 122):
            multiple = -1 if let_id >= 97 else 1
            new_str += chr(let_id + multiple * 32)
        else:
            new_str += let
    return new_str
```