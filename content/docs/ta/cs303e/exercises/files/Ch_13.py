# Exercises for Chapter 13 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)

# 13.1
# Could use r+ instead to read and write but book doesn't cover that >_>
file_name = input("Enter a filename: ")
f = open(file_name, "r")
lines = f.readlines()
lines = [x.replace("morning", "") for x in lines]
f.close()
# Book didn't cover writelines file UGH. Could just call
# f.writelines(lines)
f = open("file_name", "w")
for line in lines:
    f.write(line)
f.close()

# 13.2
file_name = input("Enter a filename: ")
f = open(file_name, "r")
lines = f.readlines()
f.close()
char_total = 0
word_total = 0
for line in lines:
    char_total += len(line)
    word_total += len(line.split())
print(char_total, " characters\n", 
        word_total, " words\n", 
        len(lines), " lines", sep="")

# 13.3
file_name = input("Enter a filename: ")
f = open(file_name, "r")
scores = f.readline().split()
f.close()
scores = [int(x) for x in scores]
total = sum(scores)
avg = sum(scores)/len(scores)
print("There are", len(scores), "scores")
print("The total is", total)
print("The average is", format(avg, ".2f"))
