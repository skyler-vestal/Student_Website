---
title: "Style"
weight: 20
---

# Python Style Guide for CS 303E

## Highlights

The following are highlighted style guidelines to follow based off the assignment page [here](https://www.cs.utexas.edu/~scottm/cs303e/Assignments/index.htm).

### Two Blank Lines

This highlight states to include two blank lines both before and after our function:

```python
# ...
# Grader: Skyler
#
#  On my honor, Skyler Vestal, this programming assignment is my own work
#  and I have not provided this code to any other student.
import random


# Here's a summary comment about the main method
def main():
    # Estimates my test scores in CS 439
    MAX_POITNS = 100
    count = random.randint(10, 20)
    print(count/MAX_POITNS)


main()
```

So the two blank lines both above `def main()` and after the last line within the main method are not overridden by comments. Always make sure there are two lines before and after!

### Four Spaces per Indent

```python
def main():
    ...
    if check_1 > num_1:
        index = 0
        count = 0
        while index < check_1:
            count += index
            if (count % 31 == 0):
                break
        print(count)
    else:
        print("Nothing.")
    ...
```

### Limitting Lines

Lines are limitted to 79 characters.

```python
def main():
    month == input("You know what a month is? Like the "
            + "arbitrary assignments of groups of days in a year.\n"
            + "Why is October the 10th month and not the 8th?\n"
            + "Why is December the 12th month and not the 10th?\n"
            + "I heard someone added in two months or something. "
            + "I'd guess July and August cause those sound like "
            + "Julius and August. Not sure.\nHow come the months "
            + "only start being numerical after August? "
            + "Why is November an exception? Strange.\n"
            + "Oh sorry, anyway enter a month: " )
    if (month == "January" or month == "February" or month == "March" or 
            month == "April" or month == "June"):
        print("This month is in the first half of the year.")
    if month == "January" or month == "June" or month == "July" \
            or month == "October":
        print("This month starts with a letter I think is weird")
```

### Limiting Comment Lines

```python
def main():
    # This line can go a fair bit out but I have to stop here sadly =(.
    print("However, I can go a bit farther out. Silly comment. Be jealous =)")
```

### Using Blank Lines

Blank lines are useful for organizing sections of code within a singular function. Make sure to make a summary comment for each non-trivial section of code.

```python
# Gather user inputs
input_1 = input("Enter a number please: ")
input_2 = eval(input("Hey uhh I'm going to trust you to enter a #: ))
input_3 = input("I feel bad for restricting you so enter anything")

# Do some arbitrary calculations
foo = input_2 ** 2 % 7
bar = ((foo * input_1) ** (3/2) - 5) % 2
outcome = ""
if bar == 0:
    outcome = "even"
else:
    outcome = "odd"

print("Sorry", input_3 + ",", "but the calculation is", outcome)
```

### Spacing

Always include a space around any operator. The one exception is keyword arguments (commented below) which occasionally include no spaces. I'd advise to still put one to be safe.

```python
if a == "some expression" or b == "an other expression":
    print(a == b)
elif a in str_list:
    print(b not in str_list)
    print(a is c)
elif a <= b:
    print(a != c)

sum = a + b
sum -= c

# The sep argument here is a keyword argument
print(a, "-", b, "-", c, sep = "")
# This also can work but to be safe do the line above. Ask your TA.
print(a, "-", b, "-", c, sep="")
```

### Cursed Variable Characters

Don't use 'l' (in "lime"), 'O' (in "Ostrich"), or 'I' (in "Italian pizza sucks") as single character variable names.

```python
# The nice syntax highlighting kinda ruins the fun but you'll get the jist 

# ... Am I adding 1, var l, or var I? Clarity will vary by text font
some_var += l
some_var += I
# Other potential problems on why l is cursed:
l = 1 | i | I
l += 1 / l
I += 1 / l * I | i

# Why O is cursed
some_var += O * 5
O = 0 + big_o(0) + o
```

### Variable Names

Python recommends [snake_case](https://en.wikipedia.org/wiki/Snake_case) (unofficial) as opposed to [camelCase](https://en.wikipedia.org/wiki/Camel_case) (official). Don't ask me why snake_case doesn't have any actual official name ¯\\\_(ツ)_/¯

```python
week = "This is a short but easily understood variable"
comment_str = "It's good to have meaning in your variables though"
descriptive_comment_str = "This is for sure on the edge of length though"
good_descriptive_comment_str = "This is way too far"
a_name_like_this = "This is also weird from the amount of words"

# Don't do camelCase
likeThis = "Avoid! This is cursedCase for this class."
```

### Main Method

We will ALWAYS have a main function in our programs. It isn't required for your program to run, but it's  beneifical for structure and [for checking if a progam is being run by itself or if it's imported from another module](https://stackoverflow.com/a/22492572). 

```python
print("This code will run.")
print("However, you're going to get a point off.")
print("So don't do it in the first place.)
```

```python
def main():
    print("This code will also run.")
    print("It gives some better structure to your program.")
    print("This will be especially relevant when we have multiple functions.")


main()
```

## Expressions

### Paranthesis

```python
# Good:
test_expr_1 = ((5 + 4) / 2 + 1) * 9 // 3 % 4

# Paranthesis can still be good if they don't change the order
# of operations if they help describe what you're doing:
# test_expr_3 is better than test_expr_2 here since it's clearer
# to see we're converting from hours -> days -> years with ()s
test_expr_2 = hours / HOURS_IN_DAY / DAYS_IN_YEAR
test_expr_3 = (hours / HOURS_IN_DAY) / DAYS_IN_YEAR

# Bad:
# Paranthesis here don't add much, so they aren't needed.
# Also may look like a tuple instead to some programmers
test_expr_4 = (5 + days // weeks)
```

### Multi-line expression

```python
# Good:
long_expression = (days_in_year * ARBITRARY_CONSTANT + months * score
                    + years * OTHER_CONSTANT)
long_expression = days_in_year * ARBITRARY_CONSTANT + months * score \
                    + years * OTHER_CONSTANT

# Okay:
# Looks kinda goofy to me when you can fit more expressions on a line
long_expression = (days_in_year * ARBITRARY_CONSTANT 
                    + months * score
                    + years * OTHER_CONSTANT)

# Bad:
# Doesn't compile
long_expression = days_in_year * ARBITRARY_CONSTANT + months * score
    + years * OTHER_CONSTANT
# Looks kinda bad with the expression to the left of the assignment)
long_expression = (days_in_year * ARBITRARY_CONSTANT + months * score
    + years * OTHER_CONSTANT)

# VERY BAD:
# This won't have a compile error but the last term won't be
# included in the expression. SCARY!
long_expression = days_in_year * ARBITRARY_CONSTANT + months * score
+ years * OTHER_CONSTANT
```

## Conditionals

### Boolean Zen

```python
# Good:
if var_1:
    print("Ah. How zenful.")

if not var_2:
    print("Still zenful.")

# Bad:
if var_1 == True:
    print("MY EYES")

if var_2 == False:
    print("EVERYTHING BURNS")
```

### Paranthesis

```python
# Good:
if (day == "Friday" or day == "Sunday") and location == "West Campus" \
        and homework is None and hour > 18:
    location = "6th Street"
    bac = .10

if (not (day == Saturday or day == Sunday) and cs_class == "439"
        and (hour >= 0 and hour <= 24)):
    homework = float("inf")
    sanity = -float("inf")
    sleep = 0
    error = "Segmentation fault"

# Bad:
if (day == "January" or day == "February"):
    print("what")

if (day == "March") or (day == "April"):
    print("still what")

if ( day == "May" or day == "June" ):
    print("still still what")
```

### if/elif/else Spacing
```python
# Good:
# Describing the first if statement condition
if condition_1:
    ...
# Describing the second if statement condition
elif condition_2:
    ...
# Describing the last if statement condition
else
    ...

# Bad:
# Describing the first if statement condition
if condition_1:
    ...

# Describing the second if statement condition
elif condition_2:
    ...

# Describing the last if statement condition
else
    ...
```

## Functions

### Calling

```python
# Good:
print(str(32) + ",")

# Bad:
print (str (32) + ",")
```

### Defining

```python
# Good:
def other_func():
    ...

def some_function(argument_1, argument_2):
    ...

# Bad:
def other_func( ):
    ...

def some_function (arg_1,arg_2) :
    ...
```

### Comments
```python
# Both acceptable:

# Given otherName, which is another name like this class's name,
# decides which of the names is first according to tie breaker
# rules and returns the first name
def breakTieBreaker(otherName):
    ...

# Break the tie breaker for the name in this class and otherName
# pre: otherName != null
# post: return the String that is seen as "best" by tiebreaker rules
def breakTieBreaker(otherName):
    ...
```

## Classes

### Declaration

```python
# This class creates an instance of NameLikeThis, that acts
# as a sheep you'd find on a farm
class FarmSheep:


    # The sheep by default has just been born with short fur
    def __init__(self, age = 0, fur_length = .1, noise = "ba"):
        self.age = age
        self.growth_factor = 38.2 / age^2
        self.fur_length = fur_length
        self.noise = noise


    # Makes the sheep let out its cry whenever scared
    def noise(self):
        print(self.noise)


    # Grows the fur of the sheep based off the amount of nutrition
    # Do sheep grow hay?
    def grow_fur(self, hay):
        # The growth of fur is based off age and hay
        growth_num = hay * self.growth_factor
        self.fur_length += growth_num
        # Nature ...
        waste = hay * .65
        return waste
```