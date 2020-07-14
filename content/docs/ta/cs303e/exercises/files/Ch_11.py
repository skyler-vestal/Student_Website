# Exercises for Chapter 11 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)
import math
import random

# 11.1
def sumColumn(m, columnIndex):
    mat_sum = 0
    for i in range(len(m)):
        mat_sum += m[i][columnIndex]
    return mat_sum

matrix = []
for i in range(3):
    user_input = input("Enter a 3-by-4 matrix row for row " + str(i) + ": ")
    row = [eval(x) for x in user_input.split()]
    matrix.append(row)
for i in range(4):
    print("Sum of the elements for column", i, "is", sumColumn(matrix, i))

# 11.2
def sumMajorDiagonal(m):
    mat_sum = 0
    for i in range(len(m)):
        mat_sum += m[i][i]
    return mat_sum

matrix = []
for i in range(4):
    user_input = input("Enter a 4-by-4 matrix row for row " + str(i + 1) + ": ")
    row = [eval(x) for x in user_input.split()]
    matrix.append(row)
print("\nSum of the elements in the major diagonal is", sumMajorDiagonal(matrix))

# 11.5
# Textbook's example output is wrong. Strange.
# Also don't worry about getting the format stuff ... at all
# Just test to make sure your addMatrix function works or else you're in
# for a rough time T_T
def addMatrix(a, b):
    res_mat = []
    for i in range(len(a)):
        row = []
        for j in range(len(b)):
            row.append(a[i][j] + b[i][j])
        res_mat.append(row)
    return res_mat

def make_matrix(entry_str):
    user_nums = input(entry_str).split()
    mat = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(eval(user_nums[i * 3 + j]))
        mat.append(row)
    return mat

def display_matrix(mats, sign):
    print("The matrices are added as follows:")
    for row in range(3):
        line = " "
        for mat in range(3):
            mat_row = ""
            for column in range(3):
                mat_row += format(mats[mat][row][column], ".1f") + " " 
                if row == 1 and column == 2:
                    if mat == 0:
                        mat_row += " " + sign
                    elif mat == 1:
                        mat_row += " ="
            line += format(mat_row, "<16")
        print(line)

# mat_1 = make_matrix("Enter matrix1: ")
# mat_2 = make_matrix("Enter matrix2: ")
# mat_3 = addMatrix(mat_1, mat_2)
# mats = [mat_1, mat_2, mat_3]
# display_matrix(mats, "+")

# 11.6
def multiplyMatrix(a, b):
    res_mat = []
    for i in range(len(a)):
        row = []
        for j in range(len(b)):
            c_sum = 0
            for k in range(3):
                c_sum += a[i][k] * b[k][j]
            row.append(c_sum)
        res_mat.append(row)
    return res_mat

mat_1 = make_matrix("Enter matrix1: ")
mat_2 = make_matrix("Enter matrix2: ")
mat_3 = multiplyMatrix(mat_1, mat_2)
mats = [mat_1, mat_2, mat_3]
display_matrix(mats, "*")

# 11.7
def min_dist(pts):
    min_dist = float("inf")
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            dist = 0
            for k in range(3):
                dist += (pts[j][k] - pts[i][k]) ** 2
            dist = math.sqrt(dist)
            min_dist = min(min_dist, dist)
    return min_dist

print(min_dist([[-1, 0, 3], [-1, -1, -1], [4, 1, 1],
                [2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3],
                [-1.5, 4, 2], [5.5, 4, -0.5]]))

# 11.13
def locateLargest(a):
    maxs = [0, 0]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > a[maxs[0]][maxs[1]]:
                maxs = [i, j]
    return maxs

rows = eval(input("Enter the number of rows in the list: "))
mat = []
for i in range(rows):
    user_input = input("Enter a row: ")
    mat.append([eval(x) for x in user_input.split()])
index = locateLargest(mat)
print("The location of the largest element is at (" + 
        str(index[0]) + ", " + (str(index[1])) + ")")

# 11.23
# I added an extra while loop to run until an even case was found
runs = 0
match = False
while not match:
    rand_mat = []
    for i in range(6):
        row = []
        for j in range(6):
            row.append(random.randint(0, 1))
        rand_mat.append(row)
    all_even = True
    row = 0
    for row in range(6):
        print(rand_mat[row])
        if all_even:
            all_even = rand_mat[row].count(1) % 2 == 0
            col = 0
            count = 0
            for col in range(6):
                if rand_mat[col][row] == 1:
                    count += 1
            all_even = all_even and count % 2 == 0
        row += 1
    result_str = "All" if all_even else "Not all"
    print(result_str, "rows and columns have an event amount of 1s")
    match = all_even
    runs += 1
print("Took", runs, "trials to finish.")