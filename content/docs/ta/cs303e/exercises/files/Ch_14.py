# Exercises for Chapter 14 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)

# 14.2
nums = input("Enter some numbers separated by spaces: ").split()
num_dict = {}
for num in nums:
    num_dict[num] = num_dict[num] + 1 if num in num_dict else 1
max_num = -1
max_list = []
for num in num_dict.keys():
    occ = num_dict[num]
    if occ > max_num:
        max_list = [num]
        max_num = occ
    elif occ == max_num:
        max_list.append(num)
# You could make this prettier if you wanted
print("Numbers that occured the most:", max_list)

# 14.4
# Are we supposed to do this one? Seems weird to mess with Tkinter

# 14.8
sort_list = []
word_file = open(input("Enter a text file: "), "r")
for line in word_file.readlines():
    for word in line.split():
        if word not in sort_list:
            sort_list.append(word)
sort_list.sort()
print(sort_list)

# 14.11
vowel_count, const_count = 0, 0
word_file = open(input("Enter a text file: "), "r")
for line in word_file.readlines():
    for word in line:
        for char in word:
            if char.isalpha():
                if char.upper() in "AEIOU":
                    vowel_count += 1
                else:
                    const_count += 1
print("Vowel Count:", vowel_count, "\nConsonant Count:", const_count)
