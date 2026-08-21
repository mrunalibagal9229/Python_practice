# 1. Write a Python program to find elements in a given set that are not in
# another set.
# Find elements in set1 that are not in set2

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result = set1 - set2

print("Elements in set1 but not in set2:", result)



# 2. Write a Python program to remove the intersection of a second set
# with a first set.
# Remove common elements of set2 from set1

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

intersection = set1 & set2
set1 -= intersection

print("Set1 after removing intersection:", set1)



# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.
# Find unique words and count their frequency

words = [
    "apple", "banana", "apple", "orange",
    "banana", "apple", "grape", "orange"
]

unique_words = set(words)

print("Unique words:", unique_words)

for word in unique_words:
    print(word, ":", words.count(word))




# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.
# Find pairs whose sum is equal to target

numbers = [2, 4, 3, 5, 7, 8, 9, 1]
target = 10

seen = set()
pairs = set()

for num in numbers:
    complement = target - num

    if complement in seen:
        pairs.add(tuple(sorted((num, complement))))

    seen.add(num)

print("Pairs whose sum is", target, ":", pairs)




# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.
# Find longest common prefix using a set

strings = ["flower", "flow", "flight"]

unique_strings = set(strings)

if not unique_strings:
    prefix = ""
else:
    prefix = min(unique_strings)

    for word in unique_strings:
        i = 0

        while i < min(len(prefix), len(word)) and prefix[i] == word[i]:
            i += 1

        prefix = prefix[:i]

print("Longest common prefix:", prefix)



# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.
# Find two numbers whose product is maximum

numbers = [-10, -5, 1, 2, 3, 8]

unique_numbers = set(numbers)

max_product = None
best_pair = None

for a in unique_numbers:
    for b in unique_numbers:
        if a != b:
            product = a * b

            if max_product is None or product > max_product:
                max_product = product
                best_pair = (a, b)

print("Two numbers:", best_pair)
print("Maximum product:", max_product)





# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.
# Find elements missing from each set

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Numbers missing in set2:", missing_in_set2)
print("Numbers missing in set1:", missing_in_set1)





# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.
# Find and group anagrams

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_groups = {}

for word in words:
    key = ''.join(sorted(word))

    if key not in anagram_groups:
        anagram_groups[key] = set()

    anagram_groups[key].add(word)

print("Anagram groups:")

for group in anagram_groups.values():
    print(group)




# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.
# Find unique combinations of 3 numbers
# whose sum equals the target

numbers = [1, 2, 3, 4, 5, 6, 7]
target = 12

unique_numbers = set(numbers)
combinations = set()

numbers_list = list(unique_numbers)

for i in range(len(numbers_list)):
    for j in range(i + 1, len(numbers_list)):
        for k in range(j + 1, len(numbers_list)):

            if numbers_list[i] + numbers_list[j] + numbers_list[k] == target:
                combination = (
                    numbers_list[i],
                    numbers_list[j],
                    numbers_list[k]
                )
                combinations.add(combination)

print("Combinations:", combinations)
