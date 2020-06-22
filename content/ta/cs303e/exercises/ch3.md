---
title: "Ch3"
date: 2020-06-22T13:53:10-05:00
draft: true
---

# Chapter 3 Exercise Solutions

Download the solution here

Embedded solutions:
```python
# Exercises for Chapter 3 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)

import math
import time

# 3.2
length = eval(input("Enter the length from the center to a vertex: "))
side = 2 * length * math.sin(math.pi / 5)
area = (3 * math.sqrt(3)/2) * side**2
print("The area of the pentagon is", round(area, 2))

# 3.3
# Using google instead
atlanta_x, atlanta_y = math.radians(33.7490), math.radians(84.3880)
orlando_x, orlando_y = math.radians(28.5383), math.radians(81.3792)
savannah_x, savannah_y = math.radians(32.0809), math.radians(81.0912)
charlotte_x, charlotte_y = math.radians(35.2271), math.radians(80.8431)
# Earth's radius is 6,371.01km
radius = 6371.01
# Get mapped distances
dist_atl_char = (radius * math.acos(math.sin(atlanta_x) * math.sin(charlotte_x)
                            + math.cos(atlanta_x) * math.cos(charlotte_x)
                            * math.cos(atlanta_y - charlotte_y)))
dist_char_sav = (radius * math.acos(math.sin(charlotte_x) * math.sin(savannah_x)
                            + math.cos(charlotte_x) * math.cos(savannah_x)
                            * math.cos(charlotte_y - savannah_y)))
dist_sav_atl = (radius * math.acos(math.sin(savannah_x) * math.sin(atlanta_x)
                            + math.cos(savannah_x) * math.cos(atlanta_x)
                            * math.cos(savannah_y - atlanta_y)))
dist_sav_orl = (radius * math.acos(math.sin(savannah_x) * math.sin(orlando_x)
                            + math.cos(savannah_x) * math.cos(orlando_x)
                            * math.cos(savannah_y - orlando_y)))
dist_orl_atl = (radius * math.acos(math.sin(orlando_x) * math.sin(atlanta_x)
                            + math.cos(orlando_x) * math.cos(atlanta_x)
                            * math.cos(orlando_y - atlanta_y)))    
print(dist_atl_char, dist_char_sav, dist_orl_atl, dist_sav_atl, dist_sav_orl)         
# Split the area into two triangles
# Triangle 1:
s_1 = (dist_atl_char + dist_char_sav + dist_sav_atl)/2
area_1 = math.sqrt(s_1 * (s_1 - dist_atl_char) 
            * (s_1 - dist_char_sav) * (s_1 - dist_sav_atl))
# Triangle 2:
s_2 = (dist_sav_orl + dist_orl_atl + dist_sav_atl)/2
area_2 = math.sqrt(s_2 * (s_2 - dist_sav_orl) 
            * (s_2 - dist_orl_atl) * (s_2 - dist_sav_atl))
final_area = area_1 + area_2
print("The area encompassed by the four cities is", 
        round(final_area, 2), "square km!")

# 3.6
input_code = eval(input("Enter an ASCII code: "))
display_chr = chr(input_code)
print("The character is", display_chr)

# 3.7
# Have only 26 possible numbers
random_code = int(time.time() % 26)
# Make the starting number A (65 + 0 = A :))
display_chr = chr(65 + random_code)
print("The random character is", display_chr)

# 3.10
print("\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6\u03b7\u03b8")
```