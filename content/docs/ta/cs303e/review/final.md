---
title: "Final"
weight: 20
---

![](/~ves314/img/study_3.gif?raw=true)

# Free Response Final Review

## Classes

### Stacks

Stacks are a commonly used data structure in computer science, and especially for memory:
![](https://www.embecosm.com/appnotes/ean3/images/prologue_frame.png?raw=true)

Quite complicated. However, the foundation of stacks is quite simple. Just think of 'em as pancakes!

![](https://www.fsrmagazine.com/sites/default/files/styles/story_image_720x430/public/feature-images/ihop-teases-another-name-change-1559147480.jpg?itok=0lbOYeVa?raw=True)

If you wanted to add to a stack, where would you add it to? Well, of course the top, since it'd be a hastle and borderline ***dangerous*** to your breakfast to lift up a bunch of pancakes for no reason. Similarly, if you were to remove from a stack, where would you remove from? Also the top. Why would you try to risk your breakfast to pick a colder pancake? As a result, elements in a stack are what are called FIFO (first-in-first-out). HEre's a video that briefly explains them as well:

{{< youtube FNZ5o9S9prU >}}

You can also watch a video of one here which is useful for evaluating mathematical expressions in computers in the correct order:

{{< youtube 7ha78yWRDlE >}}

For our purpose, we're going to make a stack class with four methods and a constructor. The methods are defined as follows:

* A constructor that takes in no parameter. This method creates a private list which will be used as the underlying data structure to act as the stack.
* A push method. This pushes a passed element onto the top of the stack.
* A pop method. This method removes an element from the top of the stack and returns it once removed.
* A peek method. This method checks out what element is currently on top of the stack without modifying the stack itself.
* A __str__ method. This method returns our underlying list as a string.

For example, the following code:
```python
stack = Stack()
stack.push(1)
stack.push(1)
stack.push(3)
print(stack.peek())
print(stack.pop())
stack.push(5)
print(stack)
```
Outputs:
```
3
3
[1, 1, 5]
```

### Fibonacci

Recall from the midterm that fibonacci numbers are defined as so:
{{< katex display >}}
F_n = F_{n - 1} + F_{n - 2}\\
F_0 = 0, F_1 = 1
{{< /katex >}}

Which means the first few fibonacci numbers are the following:
0, 1, 1, 2, 3, 5, 8, 13, ...
Essentially, the next fibonacci number is the sum of the previous two fibonacci numbers.

Create a class that generates and stores fibonacci numbers. The class contains the following methods:
* A constructor method with a single parameter. This parameter which has a default value of 10 determines how many of the first fibonacci numbers should be generated. This method should also create a list as an instance variable that will store all the fibonacci numbers, where the nth index in the list is the nth fibonacci number.
    * For example, the 0th index in the list should be 0, the 5th index in the list should be 5, and the 6th index in the list should be 8.
* A print_num method that will print the following when a number, n, is passed in:
    * If the nth fibonacci number has not been generated yet:
        * nth fibonacci number has not been generated
    * If the nth fibonacci number has been generated:
        * nth finbonacci number is (fibonacci number here)
* A gen_next method that will generate the next fibonacci number not yet generated, and this new number will be appended onto the end of the fibonacci list
* A gen_next_n method that will generate the next (as a parameter) n fibonacci numbers not yet generated, and these numbers will be appended onto the end of the fibonacci list
* A gen_until method that will generate fibonacci numbers up to (as a parameter) the nth fibonacci number.

For example, the following code:
```python
fib = Fibonacci()
fib.print_num(0)
fib.print_num(5)
fib.print_num(11)
fib.gen_next()
fib.print_num(11)
fib.gen_next_n(100)
fib.print_num(111)
fib.print_num(112)
fib.print_num(1100)
fib.gen_until(1100)
fib.print_num(1100)
```
Outputs:
```
0th fibonacci number is 0
5th fibonacci number is 5
11th fibonacci number has not been generated
11th fibonacci number is 89
111th fibonacci number is 70492524767089125814114
112th fibonacci number has not been generated
1100th fibonacci number has not been generated
1100th fibonacci number is 34428592852410271940083613070919630635781894724017874396545964292826864597491403229723364359749415183436491553996529359881593653825629442519718308678951540824183325844045884746598230684751416672062124540392876245684047939604503325
```

Fun fact: This method is extremely fast at generating fibonacci numbers as you only use the previous two result to calculate the next result. This is called caching your result, and can be thought of as a simple case of a programming strategy called [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming).

## Lists

### last_index_of

The following method is based off of a question on Mike's 2019 CS 312 Final.

Write the following function:

`def last_index_of(num_list, n)`

where num_list is a list of numbers, and n is a particular number.

The method returns a list that represents the last index of each value between [0, n] in the list.

For example, given the following list:
\\( [5, 0, 3, 12, 3, 7, 0, -3, 36]\\)
The function returns the following if n = 3: \\( [6, -1, -1, 4]\\)  
(The last appearance of 0 in the passed list was index 6, 1 and 2 never appeared in the list, and the last appearance of 3 in the passed list was index 4).

For this function, you're not allowed to use `rindex`.

### is_distinct_column_sum

Write a method is_distinct_column_sum that, given a list of lists (where each row has the same number of columns) of ints and a column index, returns true if the sum of values in each column is distinct compared to the column index in the passed list. The method is as follows:

`def is_distinct_column_sum(num_list, col_index)`

For example, in the following list of lists:
{{< katex display >}}
\begin{bmatrix}
   8 & 7 & 4 & 3 & 3 & 4 & -7 \\
   6 & 1 & 2 & 3 & 2 & 0 & 3 \\
   8 & 11 & 0 & 5 & 2 & 7 & 3 \\
   8 & 9 & 1 & 2 & 7 & 2 & -8 \\
   4 & 2 & 5 & 8 & 1 & 2 & -5 \\
\end{bmatrix}
{{< /katex >}}
The sums of columns are \\([34, 30, 12, 21, 15, 15, -14]\\). So, if the passed column index was 1, this would return true since no other column sums up to 30. However, if the passed column index was 4, this method would return false since both column 4 and 5 add up to 15.


## Dictionaries

### Counting Part 2

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

For this problem, we're going to calculate the unique combinations of any **lower-case** word passed into the following function:

`def count_unqiue_words(word)`

Samples:
```
cats: count_unqiue_words("cats") = 24
mississippi: count_unqiue_words("mississippi") = 34650
```

## Recursion

### Climbing Stairs

Let's say you got some good legs. You can either skip one stair at a time or two. However, one day during quarantine when we all have too much time, you wonder how many different combinations of climbing the stairs are possible. For example, if you had a staircase with 5 stairs. There are many different ways to climb this set with your skills:

{{< katex display >}}
[1, 1, 1, 1, 1]\\
[1, 1, 1, 2]\\
[1, 1, 2, 1]
...
{{< /katex >}}

Instead of climbing all the ways manually, you realize it may be better to create a program, that, given n amount of stairs, will determine all the different ways to climb up the stairs. 

Write the following functions

`def ways_to_climb(num_stairs, cur_list)`

Which prints out lists, where each list represents a unique way to climb the stairs.

Fun fact: The number of stair combinations based on the total number of stairs follows the [Fibonacci numbers](https://myworldtheirway.com/2019/11/its-fibonacci-sequence-day/), as the logic is really just the fibonacci algorithm in disguise.

Hint: 
The parameter cur_list for this is a bit strange, so I'll help you out. Essentially cur_list stores the current list we'll be using to track our previous steps. In this case, we don't need anything in this list to begin with, so we'll just start with it as an empty list. Consider it a temporary container we'll be using to store all the different possibilities. You should not need to delete anything from this list in your function to get the correct output. For example, a proper function call would look like:
`ways_to_climb(3, [])`

To check your answers:
```python
ways_to_climb(3, [])
```
outputs:
```python
[1, 1, 1]
[1, 2]
[2, 1]
```
and
```python
ways_to_climb(4, [])
```
outputs:
```python
[1, 1, 1, 1]
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
[2, 2]
```

### Counting Part 3

#### THIS IS WAY BEYOND THE DIFFICULTY OF WHAT Y'ALL ARE EXPECTED TO DO. PROCEED WITH CAUTION.

Based off of a random reddit thread where my reply is the answer to this question:
![](https://i.imgur.com/fDpzacF.png?raw=True)

Reference Counting Part 2 on the table of contents for the background behind permutating words. In this case, using recursion, we'll actually create all the unique permutations for a given word. Write the following function:

`def create_permutations(letter_bank, cur_word, perm_set)`

Where letter_bank is the given word we want to create permutations of, cur_word is a temporary variable to help us create permutations, and perm_set is the set of all unique word permutations of letter_bank.

Hint: Again, the setup is a bit strange for this method like with climbing stairs, so I'll help you out. letter_bank is the string of characters for our current permutation not yet used. cur_word are the letters we've used so far in our current iteration (so when we start out this will be empty). perm_set is just used to hold all of our finished permutations so far. As a result, when we start out, we want this to be empty. So some code like the following will help get you on your way for using the function. Actually programming it is up to you:

```python
word_set = set()
create_permutations("cats", "", word_set)
print(word_set)
```

As for results, here are some examples:
```python
create_permutations("cat", "", word_set)
```
outputs:
```python
{'atc', 'cat', 'tac', 'tca', 'act', 'cta'}
```

```python
create_permutations("cats", "", word_set)
```
outputs:
```python
{'cats', 'ctas', 'stac', 'tcas', 'tasc', 'tacs', 'ctsa', 'scta', 'tcsa', 'astc', 'tsca', 'atsc', 'atcs', 'csat', 'acts', 'tsac', 'satc', 'scat', 'asct', 'sact', 'acst', 'csta', 'cast', 'stca'}
```

and

```python
create_permutations("alabama", "", word_set)
```
outputs:
```python
{'baaamal', 'bamlaaa', 'maalaab', 'aaabalm', 'laaaabm', 'almbaaa', 'alambaa', 'maaalba', 'aaalmab', 'aaambla', 'aalabma', 'aaaalmb', 'abmaaal', 'aaaabml', 'blaamaa', 'aaalmba', 'ablaama', 'abaalam', 'bmalaaa', 'aalamab', 'aalmbaa', 'baamaal', 'aaablma', 'mlbaaaa', 'laaamba', 'lbamaaa', 'amabala', 'aaamlba', 'albmaaa', 'malbaaa', 'ablamaa', 'lamaaba', 'alabama', 'baaaaml', 'abaalma', 'bamalaa', 'aambaal', 'maaaabl', 'aambala', 'balaama', 'mabaala', 'aamalba', 'labamaa', 'amalaab', 'aablama', 'aabaalm', 'aablaam', 'baaaalm', 'maaaalb', 'aalbmaa', 'lambaaa', 'mbaaaal', 'malabaa', 'maalbaa', 'aamlaba', 'laabmaa', 'baalmaa', 'aaalamb', 'lbaamaa', 'amaaabl', 'alaamba', 'amlbaaa', 'amaaalb', 'lmaaaba', 'aaalabm', 'mlaaaba', 'alabaam', 'abamlaa', 'laaabma', 'lbaaama', 'lmbaaaa', 'mlaabaa', 'abalaam', 'aaaamlb', 'laamaab', 'aaalbam', 'bamaaal', 'aabamla', 'mabaaal', 'aamblaa', 'blamaaa', 'ablmaaa', 'labaama', 'lbaaaam', 'aabalam', 'abmlaaa', 'mabalaa', 'baalama', 'mlaaaab', 'bamaala', 'blaaama', 'maalaba', 'amblaaa', 'amlaaba', 
'alamaba', 'alaaamb', 'abmalaa', 'amalaba', 'aaambal', 'amaalba', 'abaamla', 'aabmaal', 'ablaaam', 'aalmaba', 'aaamalb', 'baaamla', 'bmaaala', 'amaabla', 'alamaab', 'aabmlaa', 'abamala', 'aablmaa', 'abamaal', 'aalbaam', 'aamabla', 'laambaa', 'almaaab', 'aaabaml', 'aamabal', 'maaabla', 'baaalma', 'mbalaaa', 'labmaaa', 'alabmaa', 'maaabal', 'mblaaaa', 'aamalab', 'amlabaa', 'bmlaaaa', 'laabama', 'ambaala', 'balamaa', 'baamlaa', 'malaaab', 'mbaaala', 'aalaamb', 'aaamabl', 'abaamal', 'almabaa', 'aaabmla', 'amalbaa', 'lmabaaa', 'balmaaa', 'baamala', 'laaaamb', 'albaaam', 'aamlaab', 'labaaam', 'bmaalaa', 'bmaaaal', 'albaama', 'lbmaaaa', 'aamaabl', 'laabaam', 'amlaaab', 'abaaalm', 'aalabam', 'laaamab', 'lmaabaa', 'aaaambl', 'mlabaaa', 'aabaaml', 'amaalab', 'aamlbaa', 'maabaal', 'malaaba', 'lamaaab', 'alaaabm', 'abalmaa', 'aaaablm', 'amablaa', 'balaaam', 'albamaa', 'aabamal', 'blmaaaa', 'maaalab', 'aalbama', 'ambaaal', 'abaaaml', 'mablaaa', 'amabaal', 'aabmala', 'lmaaaab', 'aabalma', 'almaaba', 'aaalbma', 'blaaaam', 'aalaabm', 'maablaa', 'amaabal', 'alaabam', 'aamaalb', 'abmaala', 'alaabma', 'laaabam', 'aaamlab', 'aaablam', 'aaabmal', 'aalamba', 'abalama', 'ambalaa', 'baalaam', 'laamaba', 'mbaalaa', 'baaalam', 'alaamab', 'aalmaab', 'lamabaa', 'aaaalbm', 
'maabala'}
```

***I'm not showing you what mississippi generates nope***

## Solutions

### Stacks
```python
class Stack:

    def __init__(self):
        self.__stack__ = []

    def push(self, elem):
        self.__stack__.append(elem)

    def pop(self):
        return self.__stack__.pop(len(self.__stack__) - 1)

    def peek(self):
        return self.__stack__[-1]
    
    def __str__(self):
        return str(self.__stack__)
```

### Fibonacci
```python
class Fibonacci:

    def __init__(self, gen_num = 10):
        self.fib_list = [0, 1]
        for i in range(gen_num - 1):
            self.gen_next()

    def print_num(self, num):
        if num < len(self.fib_list):
            print(str(num) + "th fibonacci number is", self.fib_list[num])
        else:
            print(str(num) + "th fibonacci number has not been generated") 

    def gen_next(self):
        self.fib_list.append(self.fib_list[-1] + self.fib_list[-2])

    def gen_next_n(self, n):
        for i in range(n):
            self.gen_next()

    def gen_until(self, n):
        for i in range(n - len(self.fib_list) + 1):
            self.gen_next()
```

### last_index_of
```python
def last_index_of(num_list, n):
    res_list = [-1] * (n + 1)
    for i in range(len(res_list)):
        for j in range(len(num_list)):
            if num_list[j] == i:
                res_list[i] = j
    return res_list
```

### is_distinct_column_sum
```python
def is_distinct_column_sum(num_list, col_index):
    check_sum = 0
    for row in num_list:
        check_sum += row[col_index]
    for col in range(len(num_list[0])):
        if col != col_index:
            col_sum = 0
            for row in range(len(num_list)):
                col_sum += num_list[row][col]
            if check_sum == col_sum:
                return False
    return True
```

### Counting Part 2
```python
def count_unqiue_words(word):
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    div = 1
    for i in char_count:
        div *= factorial(char_count[i])
    return factorial(len(word)) // div
    
def factorial(n):
    num = 1
    for i in range(2, n + 1):
        num *= i
    return num
```

### Climbing Stairs
```python
def ways_to_climb(num_stairs, cur_list):
    if num_stairs == 0:
        print(cur_list)
    elif num_stairs > 0:
        ways_to_climb(num_stairs - 1, cur_list + [1])
        ways_to_climb(num_stairs - 2, cur_list + [2])
```

### Counting Part 3
```python
def create_permutations(letter_bank, cur_word, perm_set):
    if len(letter_bank) == 0:
        word_set.add(cur_word)
    else:
        for i in range(len(letter_bank)):
            tmp_cur = cur_word + letter_bank[i]
            tmp_letter_bank = letter_bank[:i] + letter_bank[i + 1:]
            create_permutations(tmp_letter_bank, tmp_cur, perm_set)
```



