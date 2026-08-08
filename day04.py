#  33. Armstrong Number
def armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == n

print(armstrong(153))


# 34. Fibonacci Series
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)


# 35. Fibonacci nth Term
def fibonacci_term(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a

print(fibonacci_term(10))


# 36. GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 18))


# 37. LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(lcm(12, 18))


# 38. Power
def power(a, b):
    return a ** b

print(power(2, 5))


# 39. Percentage
def percentage(total, obtained):
    return (obtained / total) * 100

print(percentage(500, 425))


# 40. Simple Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

print(simple_interest(10000, 5, 2))


# 41. Compound Interest
def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    return amount - p

print(compound_interest(10000, 5, 2))


# 42. Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

print(celsius_to_fahrenheit(30))


# 43. Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print(fahrenheit_to_celsius(86))


# 44. Kilometer to Meter
def km_to_meter(km):
    return km * 1000

print(km_to_meter(5))


# 45. Meter to Kilometer
def meter_to_km(meter):
    return meter / 1000

print(meter_to_km(5000))


# 46. Area of Circle
def circle_area(radius):
    return 3.14159 * radius * radius

print(circle_area(5))


# 47. Circumference
def circumference(radius):
    return 2 * 3.14159 * radius

print(circumference(5))


# 48. Area of Rectangle
def rectangle_area(length, width):
    return length * width

print(rectangle_area(10, 5))


# 49. Area of Square
def square_area(side):
    return side * side

print(square_area(5))


# 50. Area of Triangle
def triangle_area(base, height):
    return 0.5 * base * height

print(triangle_area(10, 5))


# ==========================================
# STRING FUNCTIONS
# ==========================================

# 51. Reverse String
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))


# 52. String Length
def string_length(text):
    return len(text)

print(string_length("Python"))


# 53. Count Vowels
def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count

print(count_vowels("Python Programming"))


# 54. Count Consonants
def count_consonants(text):
    count = 0

    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1

    return count

print(count_consonants("Python"))


# 55. Check String Palindrome
def string_palindrome(text):
    text = text.lower()
    return text == text[::-1]

print(string_palindrome("madam"))


# 56. Count Words
def count_words(text):
    return len(text.split())

print(count_words("Python is easy"))


# 57. Uppercase
def make_upper(text):
    return text.upper()

print(make_upper("python"))


# 58. Lowercase
def make_lower(text):
    return text.lower()

print(make_lower("PYTHON"))


# 59. Capitalize
def capitalize_text(text):
    return text.capitalize()

print(capitalize_text("python programming"))


# 60. Remove Spaces
def remove_spaces(text):
    return text.replace(" ", "")

print(remove_spaces("Python Programming"))


# 61. Count Character
def count_character(text, character):
    return text.count(character)

print(count_character("banana", "a"))


# 62. First Character
def first_character(text):
    return text[0]

print(first_character("Python"))


# 63. Last Character
def last_character(text):
    return text[-1]

print(last_character("Python"))


# 64. Check Anagram
def anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

print(anagram("listen", "silent"))


# 65. Remove Duplicate Characters
def remove_duplicate_chars(text):
    result = ""

    for char in text:
        if char not in result:
            result += char

    return result

print(remove_duplicate_chars("programming"))


# 66. Count Each Character
def character_frequency(text):
    result = {}

    for char in text:
        result[char] = result.get(char, 0) + 1

    return result

print(character_frequency("banana"))


# 67. Find Vowels
def find_vowels(text):
    result = []

    for char in text:
        if char.lower() in "aeiou":
            result.append(char)

    return result

print(find_vowels("education"))


# 68. Find Longest Word
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("Python programming is powerful"))


# 69. Find Shortest Word
def shortest_word(sentence):
    words = sentence.split()
    return min(words, key=len)

print(shortest_word("Python is very easy"))


# 70. Reverse Words
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_words("Python is easy"))


# ==========================================
# LIST FUNCTIONS
# ==========================================

# 71. Sum List
def list_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(list_sum([1, 2, 3, 4, 5]))


# 72. Average List
def list_average(numbers):
    return sum(numbers) / len(numbers)

print(list_average([10, 20, 30]))


# 73. Maximum List
def list_max(numbers):
    return max(numbers)

print(list_max([10, 50, 20]))


# 74. Minimum List
def list_min(numbers):
    return min(numbers)

print(list_min([10, 5, 20]))


# 75. Count Even Numbers
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count

print(count_even([1, 2, 4, 7, 8]))


# 76. Count Odd Numbers
def count_odd(numbers):
    count = 0

    for number in numbers:
        if number % 2 != 0:
            count += 1

    return count

print(count_odd([1, 2, 3, 4, 5]))


# 77. Separate Even and Odd
def separate_even_odd(numbers):
    even = []
    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return even, odd

print(separate_even_odd([1, 2, 3, 4, 5, 6]))


# 78. Reverse List
def reverse_list(numbers):
    return numbers[::-1]

print(reverse_list([1, 2, 3, 4]))


# 79. Sort List
def sort_list(numbers):
    return sorted(numbers)

print(sort_list([5, 2, 8, 1]))


# 80. Remove Duplicates
def remove_duplicates(numbers):
    return list(set(numbers))

print(remove_duplicates([1, 2, 2, 3, 3, 4]))


# 81. Find Second Largest
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 50, 40, 50]))


# 82. Find Second Smallest
def second_smallest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[1]

print(second_smallest([10, 20, 5, 8, 5]))


# 83. Search Element
def search_element(numbers, target):
    return target in numbers

print(search_element([1, 2, 3, 4], 3))


# 84. Count Element
def count_element(numbers, target):
    return numbers.count(target)

print(count_element([1, 2, 2, 3, 2], 2))


# 85. Merge Lists
def merge_lists(a, b):
    return a + b

print(merge_lists([1, 2], [3, 4]))


# 86. Common Elements
def common_elements(a, b):
    return list(set(a) & set(b))

print(common_elements([1, 2, 3], [2, 3, 4]))


# 87. Unique Elements
def unique_elements(numbers):
    return list(set(numbers))

print(unique_elements([1, 1, 2, 3, 3]))


# 88. List Product
def list_product(numbers):
    result = 1

    for number in numbers:
        result *= number

    return result

print(list_product([1, 2, 3, 4]))


# 89. Positive Numbers
def positive_numbers(numbers):
    return [n for n in numbers if n > 0]

print(positive_numbers([-2, 3, -1, 5]))


# 90. Negative Numbers
def negative_numbers(numbers):
    return [n for n in numbers if n < 0]

print(negative_numbers([-2, 3, -1, 5]))


# ==========================================
# DICTIONARY FUNCTIONS
# ==========================================

# 91. Print Dictionary
def print_dictionary(data):
    for key, value in data.items():
        print(key, value)

print_dictionary({"name": "Mrunali", "age": 25})


# 92. Get Dictionary Keys
def dictionary_keys(data):
    return list(data.keys())

print(dictionary_keys({"a": 1, "b": 2}))


# 93. Get Dictionary Values
def dictionary_values(data):
    return list(data.values())

print(dictionary_values({"a": 1, "b": 2}))


# 94. Get Dictionary Items
def dictionary_items(data):
    return list(data.items())

print(dictionary_items({"a": 1, "b": 2}))


# 95. Search Dictionary Key
def key_exists(data, key):
    return key in data

print(key_exists({"name": "Mrunali"}, "name"))


# 96. Search Dictionary Value
def value_exists(data, value):
    return value in data.values()

print(value_exists({"a": 10, "b": 20}, 20))


# 97. Sum Dictionary Values
def dictionary_sum(data):
    return sum(data.values())

print(dictionary_sum({"a": 10, "b": 20}))


# 98. Maximum Dictionary Value
def dictionary_max(data):
    return max(data.values())

print(dictionary_max({"a": 10, "b": 50, "c": 30}))


# 99. Minimum Dictionary Value
def dictionary_min(data):
    return min(data.values())

print(dictionary_min({"a": 10, "b": 50, "c": 30}))


# 100. Invert Dictionary
def invert_dictionary(data):
    return {value: key for key, value in data.items()}

print(invert_dictionary({"a": 1, "b": 2}))


# ==========================================
# RECURSION FUNCTIONS
# ==========================================

# 101. Recursive Sum
def recursive_sum(n):
    if n == 0:
        return 0

    return n + recursive_sum(n - 1)

print(recursive_sum(10))


# 102. Recursive Fibonacci
def recursive_fibonacci(n):
    if n <= 1:
        return n

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

print(recursive_fibonacci(10))


# 103. Recursive Power
def recursive_power(a, b):
    if b == 0:
        return 1

    return a * recursive_power(a, b - 1)

print(recursive_power(2, 5))


# 104. Recursive Reverse String
def recursive_reverse(text):
    if text == "":
        return ""

    return recursive_reverse(text[1:]) + text[0]

print(recursive_reverse("Python"))


# 105. Recursive Digit Sum
def recursive_digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + recursive_digit_sum(n // 10)

print(recursive_digit_sum(12345))


# 106. Recursive Count Digits
def recursive_count_digits(n):
    if n < 10:
        return 1

    return 1 + recursive_count_digits(n // 10)

print(recursive_count_digits(12345))


# 107. Recursive Multiplication
def recursive_multiply(a, b):
    if b == 0:
        return 0

    return a + recursive_multiply(a, b - 1)

print(recursive_multiply(5, 4))


# 108. Recursive GCD
def recursive_gcd(a, b):
    if b == 0:
        return a

    return recursive_gcd(b, a % b)

print(recursive_gcd(48, 18))


# 109. Recursive List Sum
def recursive_list_sum(numbers):
    if not numbers:
        return 0

    return numbers[0] + recursive_list_sum(numbers[1:])

print(recursive_list_sum([1, 2, 3, 4]))


# 110. Recursive List Maximum
def recursive_max(numbers):
    if len(numbers) == 1:
        return numbers[0]

    return max(numbers[0], recursive_max(numbers[1:]))

print(recursive_max([10, 50, 20, 40]))


# ==========================================
# INTERMEDIATE FUNCTION PROGRAMS
# ==========================================

# 111. Calculator Function
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid Operator"

print(calculator(10, 5, "+"))


# 112. Grade Calculator
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    return "Fail"

print(grade(85))


# 113. BMI Calculator
def bmi(weight, height):
    return weight / (height ** 2)

print(bmi(60, 1.65))


# 114. Check Perfect Number
def perfect_number(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n

print(perfect_number(28))


# 115. Strong Number
def strong_number(n):
    total = 0

    for digit in str(n):
        total += factorial(int(digit))

    return total == n

print(strong_number(145))


# 116. Harshad Number
def harshad_number(n):
    return n % sum_digits(n) == 0

print(harshad_number(18))


# 117. Neon Number
def neon_number(n):
    square_value = n * n
    return sum_digits(square_value) == n

print(neon_number(9))


# 118. Automorphic Number
def automorphic(n):
    return str(n * n).endswith(str(n))

print(automorphic(25))


# 119. Spy Number
def spy_number(n):
    digits = [int(x) for x in str(n)]
    return sum(digits) == list_product(digits)

print(spy_number(123))


# 120. Duck Number
def duck_number(n):
    return "0" in str(n)[1:]

print(duck_number(1023))


# ==========================================
# DEFAULT AND KEYWORD ARGUMENTS
# ==========================================

# 121. Default Argument
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Mrunali")


# 122. Multiple Parameters
def student(name, age, course):
    print(name, age, course)

student("Mrunali", 25, "MCA")


# 123. Keyword Arguments
def employee(name, salary):
    print(name, salary)

employee(salary=50000, name="John")


# 124. Default Salary
def salary_details(name, salary=30000):
    print(name, salary)

salary_details("Rahul")
salary_details("Priya", 50000)


# 125. Variable Arguments
def total_numbers(*numbers):
    return sum(numbers)

print(total_numbers(1, 2, 3, 4, 5))


# 126. Variable Keyword Arguments
def employee_details(**details):
    for key, value in details.items():
        print(key, ":", value)

employee_details(
    name="Mrunali",
    age=25,
    city="Pune"
)


# ==========================================
# LAMBDA FUNCTIONS
# ==========================================

# 127. Lambda Addition
add_lambda = lambda a, b: a + b
print(add_lambda(10, 20))


# 128. Lambda Square
square_lambda = lambda x: x * x
print(square_lambda(5))


# 129. Lambda Even
even_lambda = lambda x: x % 2 == 0
print(even_lambda(10))


# 130. Lambda Maximum
max_lambda = lambda a, b: max(a, b)
print(max_lambda(10, 20))


# 131. Lambda Minimum
min_lambda = lambda a, b: min(a, b)
print(min_lambda(10, 20))


# 132. Lambda Cube
cube_lambda = lambda x: x ** 3
print(cube_lambda(3))


# ==========================================
# MAP, FILTER, REDUCE
# ==========================================

# 133. Map Square
def square_function(n):
    return n * n

numbers = [1, 2, 3, 4, 5]
result = list(map(square_function, numbers))
print(result)


# 134. Map Cube
def cube_function(n):
    return n ** 3

result = list(map(cube_function, numbers))
print(result)


# 135. Filter Even
def filter_even(n):
    return n % 2 == 0

result = list(filter(filter_even, numbers))
print(result)


# 136. Filter Odd
def filter_odd(n):
    return n % 2 != 0

result = list(filter(filter_odd, numbers))
print(result)


# 137. Reduce Sum
from functools import reduce

def add_values(a, b):
    return a + b

result = reduce(add_values, numbers)
print(result)


# 138. Reduce Product
def multiply_values(a, b):
    return a * b

result = reduce(multiply_values, numbers)
print(result)


# ==========================================
# MORE PRACTICE FUNCTIONS
# ==========================================

# 139. Check Alphabet
def check_alphabet(char):
    return char.isalpha()

print(check_alphabet("A"))


# 140. Check Digit
def check_digit(char):
    return char.isdigit()

print(check_digit("5"))


# 141. Check Alphanumeric
def check_alphanumeric(text):
    return text.isalnum()

print(check_alphanumeric("Python123"))


# 142. Count Uppercase
def count_uppercase(text):
    count = 0

    for char in text:
        if char.isupper():
            count += 1

    return count

print(count_uppercase("PyTHon"))


# 143. Count Lowercase
def count_lowercase(text):
    count = 0

    for char in text:
        if char.islower():
            count += 1

    return count

print(count_lowercase("PyTHon"))


# 144. Swap Two Numbers
def swap(a, b):
    return b, a

print(swap(10, 20))


# 145. Find Factors
def factors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result

print(factors(12))


# 146. Count Factors
def count_factors(n):
    return len(factors(n))

print(count_factors(12))


# 147. Check Composite
def composite(n):
    return n > 1 and not is_prime(n)

print(composite(10))


# 148. Sum of Factors
def sum_factors(n):
    return sum(factors(n))

print(sum_factors(12))


# 149. Product of Digits
def product_digits(n):
    result = 1

    while n > 0:
        result *= n % 10
        n //= 10

    return result

print(product_digits(1234))


# 150. Number of Vowels and Consonants
def vowel_consonant_count(text):
    vowels = 0
    consonants = 0

    for char in text.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants

print(vowel_consonant_count("Python"))


# ==========================================
# MINI PROJECT USING FUNCTIONS
# ==========================================

# 151. Student Details
def student_details(name, roll_no, marks):
    total = sum(marks)
    average = total / len(marks)

    print("Name:", name)
    print("Roll No:", roll_no)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade(average))


student_details(
    "Mrunali",
    101,
    [80, 75, 90, 85, 88]
)


# 152. Employee Salary
def calculate_salary(basic, allowance, deduction):
    gross = basic + allowance
    net = gross - deduction

    return gross, net

gross, net = calculate_salary(30000, 5000, 2000)

print("Gross Salary:", gross)
print("Net Salary:", net)


# 153. Bank Deposit
def deposit(balance, amount):
    return balance + amount

balance = deposit(10000, 5000)
print(balance)


# 154. Bank Withdrawal
def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount

    return "Insufficient Balance"

print(withdraw(15000, 5000))


# 155. Login Function
def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return "Login Successful"

    return "Invalid Login"

print(login("admin", "1234"))


# 156. Password Validation
def validate_password(password):
    if len(password) < 8:
        return False

    return True

print(validate_password("Python123"))


# 157. Email Validation
def validate_email(email):
    return "@" in email and "." in email

print(validate_email("test@gmail.com"))


