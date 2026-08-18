# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

s = input("Enter a string: ")

result = ""
for ch in s:
    if ch == 'a':
        result += '$'
    else:
        result += ch

print("New string:", result)




# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String
s = input("Enter a string: ")
n = int(input("Enter the index to remove: "))

result = ""
for i in range(len(s)):
    if i != n:
        result += s[i]

print("New string:", result)


# 3. Python Program to Detect if Two Strings are Anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagrams")
else:
    s1 = s1.lower()
    s2 = s2.lower()

    if sorted(s1) == sorted(s2):
        print("Anagrams")
    else:
        print("Not Anagrams")



# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged
s = input("Enter a string: ")

if len(s) <= 1:
    print(s)
else:
    new_string = s[-1] + s[1:-1] + s[0]
    print("New string:", new_string)



# 5. Python Program to Count the Number of Vowels in a String
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)


# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == ' ':
        result += '-'
    else:
        result += ch

print("New string:", result)



# 7. Python Program to Calculate the Length of a String Without Using a
# Library Function
s = input("Enter a string: ")

count = 0

for ch in s:
    count += 1

print("Length of string:", count)



# 8. Python Program to Remove the Characters of Odd Index Values in a
# String
s = input("Enter a string: ")

result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result += s[i]

print("New string:", result)




# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String
s = input("Enter a string: ")

characters = 0
words = 0
in_word = False

for ch in s:
    characters += 1

    if ch != ' ' and not in_word:
        words += 1
        in_word = True
    elif ch == ' ':
        in_word = False

print("Number of characters:", characters)
print("Number of words:", words)



# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

count1 = 0
count2 = 0

for ch in s1:
    count1 += 1

for ch in s2:
    count2 += 1

if count1 > count2:
    print("Larger string:", s1)
elif count2 > count1:
    print("Larger string:", s2)
else:
    print("Both strings have equal length")


# 11. Python Program to replace every blank space with hyphen in a string.
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == ' ':
        result += '-'
    else:
        result += ch

print("New string:", result)



# 12. Python Program to count number of lowercase characters in a string.
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch >= 'a' and ch <= 'z':
        count += 1

print("Number of lowercase characters:", count)



# 13. Python Program to count number of digits and letters in a string.
s = input("Enter a string: ")

digits = 0
letters = 0

for ch in s:
    if ch >= '0' and ch <= '9':
        digits += 1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        letters += 1

print("Number of digits:", digits)
print("Number of letters:", letters)


# 14. Python Program to count the occurrences of ach word in a string.
s = input("Enter a string: ")

words = s.split()
counted = []

for word in words:
    if word not in counted:
        count = 0

        for w in words:
            if w == word:
                count += 1

        print(word, ":", count)
        counted.append(word)



# 15. Python Program to find larger string without using built-in functions.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

count1 = 0
count2 = 0

for ch in s1:
    count1 += 1

for ch in s2:
    count2 += 1

if count1 > count2:
    print("Larger string:", s1)
elif count2 > count1:
    print("Larger string:", s2)
else:
    print("Both strings are of equal length")