---
title: "Syntax"
weight: 10
---

# Python Syntax Review for CS 303E

## Variables and Datatypes

### Types of Data
```python
# Integer datatype: Stores whole numbers like -32, 0, 66, 2332312, ...
int_var = -54

# Float datatype: Stores decimal numbers like 3.0, -2.3232, .00033,
# 5.6e+15
float_var = -.04

# Boolean datatype: Stores the value true or false
bool_var = True
bool_var = False

# String datatype: Stores any word
str_var = "You can use double quotes"
str_var = 'or single quotes for strings'
```

### Modification
```python
# These two are the same
# This works for +, -, *, /, //, %, **
int_var = int_var + 5
int_var += 5

# Operators examples
10 / 3  # == 3.3333333333333335
10 // 3 # == 3
10 % 3  # == 1
10 ** 3 # == 1000

# Negative division
-10 / 3  # == -3.3333333333333335
-10 // 3 # == -4
-10 % 3  # == 2
10 ** -3 # == .001

# Boolean negation
not True  # == False
not False # == True

# Concatenation
"This is an example of " + "concatenation"
str_var = "This is also an example of"
str_var += " concatenation"
```

## Input / Output

### Concatenation
```python
# Output: Mike Scott teaches 1 class on MWTH
print("Mike Scott teaches 1 class on MWTH")
print("Mike Scott teaches " + str(1) + " class on MWTH")
print("Mike", "Scott", "teaches", 1, "class", "on", "MWTH")
print("Mike ", "Scott ", "teaches ", 1, " class ", "on ", "MWTH", sep="")
print("Mike ", "Scott ", "teaches ", str(1) + " class ", "on ", "MWTH", sep="")

# Doesn't work - Can't concatenate non String datatypes
print("Mike Scott teaches " + 1 + " class on MWTH")
```

### Multi-line Outputs
```python
'''Output:
    This is line 1
    This is line 2
'''
print("This is line 1")
print("This is line 2")

# Output: This is one line. This is on the same line
print("This is one line. ", end="")
print("This is on the same line")
```


### Multi-line Strings
```python
# Best way
print("In case your string is " +
        "a bit too long")

# Works but looks bad
print("In case your string is \
a bit too long")
print("""In case your string is
a bit too long""")

# Doesn't work (too many spaces)
print("In case your string is \
        a bit too long")
print("""In case your string is
        a bit too long""")
```

### Escape Sequences
```python
''' Output:
        This is line 1
        This is line 2
'''
print("This is line 1\nThis is line 2")

# Output: This is line 1    This is line 2
print("This is line 1\tThis is line 2)
```

### Handling Input
```python
''' Output:
        Enter user input: [input]
        What you typed: [user input relayed]
'''
user_input = input("Enter user input: ")
print("What you typed:", user_input)

''' Output:
        Enter an integer: [input]
        Input num squared: [input^2]
'''
num = eval(input("Enter an integer: "))
print("Input num squared:", str(num ** 2))
```

## Libraries

### Importing
```python
import math
math.sqrt(9)
math.floor(4.3)

import math as m
m.sqrt(9)
m.floor(4.3)

from math import sqrt, floor
sqrt(9)
floor(4.3)
```

## Conditionals

### Logical Operators
```python
True == True  # True
True == False # False

4 == 4 # True
4 == 5 # False

"UT" == "UT"  # True
"UT" == "UTe" # False
"UT" == "UT " # False

not True  # False
not False # True

True != False    # True
True != True     # False
True != not True # ... True

True and True   # True
True and False  # False
False and False # False

True or True   # True
True or False  # True
False or False # False
```

### Comparison Operators
```python
# Technically == and != are comparison operators

5 > 4 # True
4 > 4 # False
3 > 4 # False
5 > 4 > 3 # True

5 >= 4 # True
4 >= 4 # True
3 >= 4 # False

5 < 4 # False
4 < 4 # False
3 < 4 # True
3 < 4 < 5 # True

5 <= 4 # False
4 <= 4 # True
3 <= 4 # True
```

### if Statements
```python
if True:
    print("This always prints")
    print("There can be multiple lines")

if var_1 == var_2 or var_2 == var_3:
    print("Two variables are equal")

if var_1 == var_2 and var_2 == var_3:
    print("All three variables are equal")

# If the conditional is a string tests if the
# string is non-empty
if "abc":
    print("This always prints")

if "":
    print("This never prints")

# If the conditional is a number tests if the
# number is not zero
if 1:
    print("This always prints")

if 0:
    print("This never prints")
```

### Multi-line conditions
```python
if var_1 == var_2 or var_1 == var_3 or \
        var_1 == var_4:
    print("Var 1 equals some other variable")

if (var_1 == var_2 and var_1 == var_3 and 
        var_1 == var_4):
    print("All variables are equal")
```

### if/elif/else Statements
```python
if (month == "December" or month == "January"
        or month == "February"):
    print("It's winter")
elif (month == "March" or month == "May"
        or month == "April"):
    print("It's spring")
elif (month == "June" or month == "July"
        or month == "August"):
    print("It's summer")
else:
    print("It's fall! My favorite.")
```


## Iteration

### while Loops
```python
count = 0
total = 0
while count < 1000:
    total += count

count = 0
total = 0
while count < 1000 and not (count > 100 and count % 17 != 0):
    total += count
```

### for Loops
```python
# Output: 0 1 2 ... 9
for i in range(10):
    print(str(i) + " ")

# Output: 3 4 5 ... 9
for i in range(3, 10):
    print(str(i) + " ")

# Output: 3 5 7 ... 19
for i in range(3, 20, 2):
    print(str(i) + " ")  
```