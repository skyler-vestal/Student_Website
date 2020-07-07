---
title: "Midterm"
weight: 10
---

![](/~ves314/img/study_2.gif?raw=true)

# Midterm Review

## MC/Short Answer Section

### Noah's Multiple Choice

Noah (fellow TA) has made a lot of great multiple choice questions that he's decided to share with me. Big :clap: for him.

**Assume libraries have been imported correctly for the following questions.**

1. What is output by the following code?
```python
x = int(52.2)
y = math.floor(999.9)
print(x, y)
```
```
A. 52 1000
B. 52 999
C. 52.0 999.0
D. 52.0 1000.0
```

2. What is output by the following code?
```python
t = math.floor(-909.1)
a = int(-49.1)
print(t, a)
```
```
A. -908 -49
B. -909 -50
C. -910 -50
D. -908 -50
E. -909 -49
F. -910 -49
```

3. What is output by the following code?
```python
y = math.floor(-3.99 - .01)
j = math.floor(5.99 + .1)
print(y, j)
```
```
A. -3 5
B. -4 5
C. -3 6
D. RUNTIME ERROR
E. -4 6
```

4. What is output by the following code?
```python
m = int(52.9 + .1)
print(m)
```
```
A. 53.0
B. 52
C. RUNTIME ERROR
D. 52.0
E. 53
```

5. What is output by the following code?
```python
p = 10 // 3
q = 3 // 10
print(p, q)
```
```
A. 3.0 3.0
B. 3 3
C. 3.0 0.0
D. 3 0
```

6. What is output by the following code?
```python
y = 4 / 2
a = 2 % 6
print(y, a)
```
```
A. 2.0 2.0
B. 2 2
C. 2 0
D. 2.0 0.0
E. 2.0 2
```

7. What is output by the following code?
```python
f = 9 % -4
g = -7 % 13
print(f, g)
```
```
A. -3 -6
B. -1 -7
C. -3 6
D. 1 -7
```

8. What is output by the following code?
```python
x = 2
y = x - 2
x *= 2
y += -1
print(x, y)
```
```
A. 0, 1
B. 4 1
C. 0 -1
D. 4 -1
```

9. What is output by the following code?
```python
x = eval('4')
y = int('-23')
print(y, x)
```
```
A. 4 23
B. -23 4
C. 23 -4
D. SYNTAX ERROR
E. RUNTIME ERROR
```

10. What is output by the following code?
```python
x = eval('9 + 1')
print(x)
```
```
A. 9 + 1
B. SYNTAX ERROR
C. RUNTIME ERROR
D. 10
E. 10.0
```

11. What is output by the following code?
```python
t = int('1 - 1')
print(t)
```
```
A. SYNTAX ERROR
B. 1 - 1
C. RUNTIME ERROR
D. 0
E. 0.0
```

12. What is output by the following code?
```python
k = eval('99.0 + 1')
print(k)
```
```
A. RUNTIME ERROR
B. 100.0
C. SYNTAX ERROR
D. 100
```

13. What is output by the following code?
```python
x = 2
y = 4
z = 9
if x <= 2 and y > 4:
    print('case1')
elif z < 9 or x >= 2:
    print('case2')
else:
    print('case3')
```
```
A. case2
B. case3
C. case1
```

14. What is output by the following code?
```python
count = 0
x = 'A'
y = 'B'
if x == 'X' or y == x:
    count += 1
elif count < 50 and y == 'B':
    count += 5
else:
    count *= 3
count *= 2
print(count)
```
```
A. 8
B. 2
C. 10
D. 5
E. 1
```

15. What is output by the following code?
```python
import random
num = random.randint(0,1)
if num == 0:
    print(num)
elif num == 1:
    print(num - 1)
else:
    print(50)
```
```
A. 1
B. 0
C. Impossible to Determine
D. 50
```

16. What is output by the following code?
```python
x = 1
y = '1'
a = x == y and x > 0
b = y != '1' or x % 5 >= 1
print(a, b)
```
```
A. True True
B. False True
C. True False
D. False False
```

17. What is output by the following code?
```python
count = 0
for i in range(0, 10):
    count *= 2
print(count)
```
```
A. 1024
B. 2
C. 0
D. 20
```

18. What is output by the following code?
```python
loop_control = 1
count = 0
while loop_control < 10:
    loop_control *= 2
    count += 1
print(count)
```
```
A. 6
B. 4
C. 3
D. 10
E. 5
```

19. What is output by the following code?
```python
what_am_i = 0
for i in range(50):
    what_am_i = i
print(what_am_i)
```
```
A. RUNTIME ERROR
B. 50
C. 49
D. 1
```

20. What is output by the following code?
```python
loop_control = -2
while loop_control < 50:
    loop_control += 1
print(loop_control)
```
```
A. 51
B. 48
C. 50
D. 49
```

21. What is output by the following code?
```python
count = 0
for i in range(3, 15, 3):
    count += 1
print(count)
```
```
A. 3
B. INFINITE LOOP
C. 5
D. 4
```

22. What is output by the following code?
```python
loop_control = -10
while loop_control <= 0:
    loop_control *= 2
print(loop_control)
```
```
A. INFINITE LOOP
B. 1
C. 20
D. 0
```

23. What is output by the following code?
```python
count = 0
for i in range(10, 0, -1):
    count += 1
print(count)
```
```
A. 0
B. INFINITE LOOP
C. 10
D. 11
E. 9
```

24. What is output by the following code?
```python
def a(x):
    x = b(x)
    return x + 2

def b(y):
    return y * 2

what_am_i = a(5)
print(what_am_i)
```
```
A. 7
B. 9
C. 10
D. 12
```

25. What is output by the following code?
```python
def a(x, y):
    x = 3
    y = 3
    return x * y

def b(z, t):
    z += 2
    t = a(z, t)
    return z * t

what_am_i = b(0, 0)
print(what_am_i)
```
```
A. 18
B. 0
C. 9
D. 27
```

26. What is output by the following code?
```python
def a(x, y):
    return x + y

def b(z, t):
    z = 0
    t = 1
    return a(z, t)

z = 50
t = 0
print(b(z, t), z, t)
```
```
A. 1 0 1
B. 50 0 1
C. 50 50 0
D. 1 50 0
```

### CS 312 Fall '19

The following is Mike's CS 312 Exam 1 from Fall 2019 and 2018. You can find the original page [here](https://www.cs.utexas.edu/~scottm/cs312/testStudyMaterials.htm). I've translated a few questions from Java to Python

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

### Original Questions

#### Level 1 Difficulty

#### 3x3 Determinant

A determinant is a very useful calculation in linear algebra that can tell you how much an area or volume shrinks or grows when you squish and stretch out an area of space.
{{< youtube Ip3X9LOh2dk >}}
The video above is awesome if you want an intuitive feel for what this exactly means, and why the following calculations are the way they are. This video isn't required to be watch to write the following function.

Consider a \\( 2 \times 2 \\) determinant calculation:

{{< katex display >}}
\text{det}
\begin{bmatrix}
   a & b \\
   c & d
\end{bmatrix} = ad - bc
{{< /katex >}}

In terms of Python, this can be implemented with the following function:
```python
def det_2x2(a, b, c, d):
    return a * d - b * c
```
In your case, use this function written above to make the process of calculating the determinannt of a \\(3 \times 3\\) matrix easier:

{{< katex display >}}
\text{det}
\begin{bmatrix}
   a & b & c \\
   d & e & f \\
   g & h & i
\end{bmatrix} = 
a \cdot \text{det}\begin{bmatrix}
   e & f \\
   h & i
\end{bmatrix} -
b \cdot \text{det}\begin{bmatrix}
   d & f \\
   g & i
\end{bmatrix} +
c \cdot \text{det}\begin{bmatrix}
   d & e \\
   g & h
\end{bmatrix}
{{< /katex >}}

Implement:

`def det_3x3(a, b, c, d, e, f, g, h, i)`

using `def det_2x2(a, b, c, d)` described above.   
The function returns the determinant of the 3x3 matrix.

#### Level 2 Difficulty

#### 1 Dimensional Random Walker

A 1D random walker is an agent that starts at the poisition 0 on a number line. Every turn, the agent has a 50% chance of moving left one unit to -1, and a 50% chance of moving right one unit to 1. As a result, the random walker will appear to dart back and fourth on the number line forever if you don't give it any constraints. In this case, we want to run the random walker until our agent is \\( n \\) units away from its starting location

Implement:

`def random_walker_1d(n)`

where \\( n \\) represents the distance from the agent to its starting point. The simulation will stop once this distance is reached
The function will return 2 parameters. The first represents the total moves required to reach this distance, and the second represents the average position of this random walker on its journey to this location.

Samples:
```
Seed = "Mike Scott":
random_walker_1d(10) = (64, -1.875)
random_walker_1d(25) = (189, -9.645502645502646)
random_walker_1d(50) = (1562, -22.51920614596671)
random_walker_1d(100) = (2104, -35.163498098859314)
random_walker_1d(300) = (21250, -169.24823529411765)
random_walker_1d(500) = (82660, -272.5082748608759)
random_walker_1d(1000) = (1989318, -233.90734362228665)
random_walker_1d(5000) = (16308946, 284.5807719885761)
```

#### Level 3 Difficulty

##### Counting Part 1

Counting in probability and discrete math have a more complete meaning than the every day meaning. Essentially, counting is determining the total number of elements in a set. This really is what we do when we count normally, but this can be taken much further:

In mathematics, if you have \\(n\\) unique objects together, the amount of unique orderings is simply:

{{< katex display >}}
\text{Unique Combinations} = n!\\

n! = n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot 3 \cdot 2 \cdot 1
{{< /katex >}}

This can be used to calculate the number of unique orderings of letters in a word. For example, according to this formula, cat should have 6 unique ordering of letters since there are 3 unique letters, so \\(n = 3\\):

| # | Word | # | Word |
| :--- | :--- | :--- | :--- |
| 1 | cat | 3 | tca |
| 2 | cta | 4 | tac |
| 5 | act | 6 | atc |

However, consider the case with eel. If all three letters were unique there would be 6 unique combinations, but since there are two es, how many combinations can we really make?

| # | Word |
| :--- | :--- |
| 1 | eel |
| 2 | ele |
| 3 | lee |

As it turns out, the more useful formula for unique combinations is as follows, where \\( a_k \\) is the # of occurences of the identical objects in the entire group. For example, in eel, \\( a_e = 2 \\):

$$
\text{Unique Combinations} = \dfrac{n!}{a_1!a_2! ... a_k!}
$$

For this problem, we're going to calculate the unique combinations of **lower-case** words where there are 4 unique letters in the **lower-case word**. For example, dogs and mississippi both have 4 unique letters. Implement:

`def count_unqiue_words(letter_1, letter_2, letter_3, letter_4)`

For each parameter in the function, the parameter stores the number of occurences of that letter, so letter_1 for mississippi stores 1 for 1 occurence of m, whereas letter_2 stores 4 because of 4 is. The function returns the number of words from the letters given in the parameters. 

Samples:
```
cats: count_unqiue_words(1, 1, 1, 1) = 24
mississippi: count_unqiue_words(1, 4, 4, 2) = 34650
```


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

### MC/Short Answers

#### Noah's MC
```
1. B
2. F
3. E
4. E
5. D
6. E
7. C
8. D
9. B
10. D
11. C
12. B
13. A
14. C
15. B
16. B
17. C
18. B
19. C
20. C
21. D
22. A
23. C
24. D
25. A
26. D
```

#### Fall '19
```
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
```

#### Fall '18
```
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

#### Original Questions

```python
# Level 1 Difficulty
def det_3x3(a, b, c, d, e, f, g, h, i):
    return a * det_2x2(e, f, h, i) - b 
        * det_2x2(d, f, g, i) + c * det_2x2(d, e, g, h)

def det_2x2(a, b, c, d):
    return a * d - b * c



# Level 2 Difficulty
from random import randint

def random_walker_1d(n):
    moves = 0
    x = 0
    total = 0
    while abs(x) < n:
        # Makes random numbers only -1 and 1. More straight forward code
        # to just use an if statement
        x += (randint(0, 1) * 2) - 1
        moves += 1
        total += x
    return moves, total/moves



# Level 3 Difficulty
def count_unqiue_words(letter_1, letter_2, letter_3, letter_4):
    total = letter_1 + letter_2 + letter_3 + letter_4
    n = factorial(total)
    let_1_factor = factorial(letter_1)
    let_2_factor = factorial(letter_2)
    let_3_factor = factorial(letter_3)
    let_4_factor = factorial(letter_4)
    return n / (let_1_factor * let_2_factor * let_3_factor * let_4_factor)

def factorial(n):
    num = 1
    for i in range(2, n + 1):
        num *= i
    return num
```

#### HackerRank
```python
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

Colette made me put this:  
![](/~ves314/img/ein.gif?raw=true)