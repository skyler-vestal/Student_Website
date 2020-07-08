---
title: "A9 Tester"
weight: 60
---

# Test File for Assignment 9

Hey! I've created a test file to help with your current assignment, since entering all of Mike's inputs is quite tedious while troubleshooting. Additionally, I've created methods to generate random tests along with easily testing the other functions yourself with custom inputs!

[Click here to access the file](strings_tester.py)

## Steps to Install
1. Access the file
2. Right click on the file and select "Save as" or something similar
3. Move this file into the same folder as your strings.py
4. In strings.py, at the bottom of the program change it so it looks like:
```python
if __name__ == "__main__":            
    main()
```
(MAKE SURE TO REMOVE THIS WHEN YOU'RE DONE TESTING AND WILL SUBMIT)
5. Run the strings_tester.py file!

## Mike's Outputs

### Example 1
```
----- EXAMPLE 1 -----
--------------------
Function name: num_chars_same
Parameter 1: catch
Parameter 2: cots
Return value: 2
--------------------
--------------------
Function name: num_chars_same
Parameter 1: catch
Parameter 2: cat chaser
Return value: 3
--------------------
--------------------
Function name: stretch
Parameter 1: dog
Parameter 2: 3
Return value: dddooooooggggggggg
--------------------
--------------------
Function name: stretch
Parameter 1: dog
Parameter 2: 1
Return value: dooggg
--------------------
--------------------
Function name: length_of_matching_suffix
Parameter 1: cat
Parameter 2: doggo
Return value: 0
--------------------
--------------------
Function name: length_of_matching_suffix
Parameter 1: dog
Parameter 2: doggo
Return value: 0
--------------------
```

### Example 2
```
----- EXAMPLE 2 -----        
--------------------
Function name: num_chars_same
Parameter 1: catch
Parameter 2: batches
Return value: 4
--------------------
--------------------
Function name: stretch
Parameter 1: dog
Parameter 2: 0
Return value:
--------------------
--------------------
Function name: length_of_matching_suffix
Parameter 1: cats
Parameter 2: dogs
Return value: 1
--------------------
```

### Example 3
```
----- EXAMPLE 3 -----
--------------------
Function name: num_chars_same
Parameter 1: dog
Parameter 2: cats
Return value: 0
--------------------
--------------------
Function name: num_chars_same
Parameter 1:
Parameter 2: cats
Return value: 0
--------------------
--------------------
Function name: num_chars_same
Parameter 1: Hamilton
Parameter 2: ham stands!
Return value: 4
--------------------
--------------------
Function name: stretch
Parameter 1: Dogs!
Parameter 2: 4
Return value: DDDDooooooooggggggggggggssssssssssssssss!!!!!!!!!!!!!!!!!!!!
--------------------
--------------------
Function name: stretch
Parameter 1: 1234
Parameter 2: 2
Return value: 11222233333344444444
--------------------
--------------------
Function name: stretch
Parameter 1: !!!
Parameter 2: 1
Return value: !!!!!!
--------------------
--------------------
Function name: length_of_matching_suffix
Parameter 1: cats
Parameter 2:
Return value: 0
--------------------
--------------------
Function name: length_of_matching_suffix
Parameter 1: cats
Parameter 2: maniacs
Return value: 1
--------------------
--------------------
Function name: length_of_matching_suffix
Parameter 1: dog
Parameter 2: cat and dog
Return value: 3
--------------------
```

## Random Output Sample
```
Enter one of the following
    - m to Mike's same example
    - r to run random tests
    - s to select a certain method

Your choice: r
Enter the number of random tests: 5
Enter a # for the seed for the test: 69
--------------------
Function name: length_of_matching_suffix
Parameter 1: PDXl
Parameter 2: HikdDoZxUUJcvdTepMnFadueMeudLjhgTDXl
Return value: 3
--------------------
--------------------
Function name: length_of_matching_suffix
Parameter 1: QXBhDVxF
Parameter 2: QXBhDVxF
Return value: 8
--------------------
--------------------
Function name: stretch
Parameter 1: PYqEDYyPVzmyhw
Parameter 2: 0
Return value:
--------------------
--------------------
Function name: stretch
Parameter 1: RauNxsfxJHZLdBz
Parameter 2: 1
Return value: RaauuuNNNNxxxxxssssssfffffffxxxxxxxxJJJJJJJJJHHHHHHHHHHZZZZZZZZZZZLLLLLLLLLLLLdddddddddddddBBBBBBBBBBBBBBzzzzzzzzzzzzzzz
--------------------
--------------------
Function name: length_of_matching_suffix
Parameter 1: SBydmzuxBJwN
Parameter 2: kaoVFcoOpFGrMnPZbASpMsQnEZXWzuxBJwN
Return value: 7
--------------------

Tests done. Enter y to do more tests: n
```

## Custom Input Sample
```
Enter one of the following
    - m to Mike's same example
    - r to run random tests
    - s to select a certain method

Your choice: s
Enter the number of select tests: 3

Enter a function choice number:
     - 0 for num_chars_same
     - 1 for stretch
     - 2 for length_of_matching_suffix
Enter your function number choice: 0
--------------------
Trial #: 1
Function name: num_chars_same
First parameter: sample string
Second parameter: sample word
Return value: 8
--------------------

Enter a function choice number:
     - 0 for num_chars_same
     - 1 for stretch
     - 2 for length_of_matching_suffix
Enter your function number choice: 1
--------------------
Trial #: 2
Function name: stretch
First parameter: beanin'
Second parameter: 7
Return value: bbbbbbbeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaannnnnnnnnnnnnnnnnnnnnnnnnnnniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'''''''''''''''''''''''''''''''''''''''''''''''''
--------------------

Enter a function choice number:
     - 0 for num_chars_same
     - 1 for stretch
     - 2 for length_of_matching_suffix
Enter your function number choice: 2
--------------------
Trial #: 3
Function name: length_of_matching_suffix
First parameter: eeeeeeEEEEEEE
Second parameter: REEEEEEEEEEE
Return value: 7
--------------------

Tests done. Enter y to do more tests: n
```

Here's Colette's dog Hunter:

![](/~ves314/img/hunter.jpg?raw=true)