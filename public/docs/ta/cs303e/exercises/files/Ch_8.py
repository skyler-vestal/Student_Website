# Exercises for Chapter 8 of "Introduction to Programming using Python"
# Solutions made by Skyler Vestal (Hook 'Em)

# 8.1
# Look up Regular Expressions to see how string checks are normally done =)
ssn = input("Enter a Social Security number: ")
ssn_valid = True
ssn_valid = len(ssn) == 11
index = 0
while ssn_valid and index < len(ssn):
    if index == 3 or index == 6:
        ssn_valid = ssn[index] == '-'
    else:
        ssn_valid = ssn[index].isnumeric()
    index += 1
valid_str = "Valid" if ssn_valid else "Invalid"
print(valid_str, "SSN")

# 8.3
pw = input("Enter your ... password?: ")
pw_valid = len(pw) >= 8
digits = 0
index = 0
while pw_valid and index < len(pw) and digits < 2:
    if pw[index].isnumeric():
        digits += 1
    elif not pw[index].isalpha():
        pw_valid = False
    index += 1
valid_str = "valid" if ssn_valid else "invalid"
print(valid_str, "password")

# 8.7
def getNumber(uppercaseLetter):
    if uppercaseLetter.isalpha():
        if uppercaseLetter <= "O":
            let_ascii = ord(uppercaseLetter) - 65
            phone_num = let_ascii // 3 + 2
        # Eh just cut your losses and check it manually
        elif uppercaseLetter <= "S": phone_num = 7
        elif uppercaseLetter <= "V": phone_num = 8
        else: phone_num = 9
    else:
        phone_num = int(uppercaseLetter)
    return phone_num

phone_str = input("Enter a string: ")
phone_num = ""
for let in phone_str:
    if let.isalpha():
        phone_num += str(getNumber(let.upper()))
    elif let.isnumeric():
        phone_num += str(getNumber(let))
    else:
        phone_num += let

# 8.12
genome = input("Enter a genome string: ")
start_gene = False
curr_gene = ""
start = False
for nuc in genome:
    # Keep a string of the current genes to consider
    curr_gene += nuc
    if len(curr_gene) >= 3:
        last_trip = curr_gene[-3:]
        # If we hit a start gene and aren't recording then start recording
        if not start and last_trip == "ATG":
            start = True
            curr_gene = ""
        # If we are recording and hit an end gene stop 
        # and print the current result
        elif start and (last_trip == "TAG" or 
                last_trip == "TAA" or last_trip == "TGA"):
            start = False
            print(curr_gene[:-3])
            curr_gene = ""
# if we never hit a start then all of genome is in curr_gene
if curr_gene == genome:
    print("no gene is found")
        
# 8.13
def prefix(s1, s2):
    prefix = ""
    index = 0
    small_len = min(len(s1), len(s2))
    still_same = True
    while still_same and index < small_len and s1[index] == s2[index]:
        prefix += s1[index]
        index += 1
    return prefix

# Not writing a main function for the sake of the format of this page
s1 = input("Enter a string (1): ")
s2 = input("Enter a string (2): ")
print("Common prefix between strings:", prefix(s1, s2))

# 8.15
isbn = input("Enter the first 9 digits of an ISBN-10 as a string: ")
curr_num = 0
for index in range(len(isbn)):
    curr_num += (index + 1) * int(isbn[index])
last_num = curr_num % 11
last_num = "X" if last_num == 10 else str(last_num)
print("The ISBN-10 number is", isbn + last_num)