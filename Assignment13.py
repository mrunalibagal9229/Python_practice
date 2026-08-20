# 1. Python Program to Add a Key-Value Pair to the Dictionary
# Add a key-value pair to a dictionary

my_dict = {"name": "John", "age": 20}

my_dict["city"] = "Pune"

print("Updated dictionary:", my_dict)


# 2. Python Program to Concatenate Two Dictionaries Into One
# Concatenate two dictionaries

dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

dict1.update(dict2)

print("Combined dictionary:", dict1)


# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not
# Check if a key exists

my_dict = {"name": "John", "age": 20, "city": "Pune"}

key = input("Enter the key to search: ")

if key in my_dict:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")


# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).
# Generate dictionary containing numbers from 1 to n
# in the form (x, x*x)

n = int(input("Enter the value of n: "))

my_dict = {}

for x in range(1, n + 1):
    my_dict[x] = x * x

print("Generated dictionary:", my_dict)


# 5. Python Program to Sum All the Items in a Dictionary
# Sum all values in a dictionary

my_dict = {"a": 10, "b": 20, "c": 30, "d": 40}

total = sum(my_dict.values())

print("Sum of all items:", total)



# 6. Python Program to Multiply All the Items in a Dictionary
# Multiply all values in a dictionary

my_dict = {"a": 2, "b": 3, "c": 4}

product = 1

for value in my_dict.values():
    product = product * value

print("Product of all items:", product)



# 7. Python Program to Remove the Given Key from a Dictionary
# Remove a given key from a dictionary

my_dict = {"name": "John", "age": 20, "city": "Pune"}

key = input("Enter the key to remove: ")

if key in my_dict:
    del my_dict[key]
    print("Updated dictionary:", my_dict)
else:
    print("Key does not exist.")



# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary
# Count frequency of words in a string

text = input("Enter a string: ")

words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)