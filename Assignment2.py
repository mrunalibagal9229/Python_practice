# # Convert Time (hh, min, sec) into Seconds
# hours = int(input("Enter hours: "))
# minutes = int(input("Enter minutes: "))
# seconds = int(input("Enter seconds: "))

# total_seconds = (hours * 3600) + (minutes * 60) + seconds

# print("Total Seconds =", total_seconds)


# Convert Celsius to Fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 9/5) + 32

# print("Temperature in Fahrenheit =", fahrenheit)

# Convert Distance from Feet and Inches into Meters and Centimeters
# 

# Calculate Area of Triangle and Rectangle
# # Triangle
# base = float(input("Enter base of triangle: "))
# height = float(input("Enter height of triangle: "))

# triangle_area = 0.5 * base * height

# # Rectangle
# length = float(input("Enter length of rectangle: "))
# breadth = float(input("Enter breadth of rectangle: "))

# rectangle_area = length * breadth

# print("Area of Triangle =", triangle_area)
# print("Area of Rectangle =", rectangle_area)

# Calculate Selling Price of Book
# cost_price = float(input("Enter Cost Price: "))
# discount = float(input("Enter Discount Percentage: "))

# selling_price = cost_price - (cost_price * discount / 100)

# print("Selling Price =", selling_price)

# Calculate Total Salary of Employee
# basic = float(input("Enter Basic Salary: "))

# da = basic * 0.10
# ta = basic * 0.12
# hra = basic * 0.15

# total_salary = basic + da + ta + hra

# print("DA =", da)
# print("TA =", ta)
# print("HRA =", hra)
# print("Total Salary =", total_salary)

# Find Sum of Three-Digit Number
# num = int(input("Enter a three-digit number: "))

# digit1 = num // 100
# digit2 = (num // 10) % 10
# digit3 = num % 10

# sum_digits = digit1 + digit2 + digit3

# print("Sum of digits =", sum_digits)

# Swap Two Numbers Using Third Variable
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# temp = a
# a = b
# b = temp

# print("After Swapping:")
# print("a =", a)
# print("b =", b)

# Swap Two Numbers Without Using Third Variable
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# a = a + b
# b = a - b
# a = a - b

# print("After Swapping:")
# print("a =", a)
# print("b =", b)

# Reverse a Three-Digit Number
# num = int(input("Enter a three-digit number: "))

# digit1 = num // 100
# digit2 = (num // 10) % 10
# digit3 = num % 10

# reverse = digit3 * 100 + digit2 * 10 + digit1

# print("Reversed Number =", reverse)

# Minimun Number of notes required

# amount = int(input("Enter amount: "))

# notes_500 = amount // 500
# amount %= 500

# notes_200 = amount // 200
# amount %= 200

# notes_100 = amount // 100
# amount %= 100

# notes_50 = amount // 50
# amount %= 50

# notes_20 = amount // 20
# amount %= 20

# notes_10 = amount // 10
# amount %= 10

# print("500 Notes =", notes_500)
# print("200 Notes =", notes_200)
# print("100 Notes =", notes_100)
# print("50 Notes =", notes_50)
# print("20 Notes =", notes_20)
# print("10 Notes =", notes_10)
# print("Remaining Amount =", amount)