# Calculate percentage of student
# m1 = float(input("Enter marks of Subject 1: "))
# m2 = float(input("Enter marks of Subject 2: "))
# m3 = float(input("Enter marks of Subject 3: "))
# m4 = float(input("Enter marks of Subject 4: "))
# m5 = float(input("Enter marks of Subject 5: "))

# total = m1 + m2 + m3 + m4 + m5
# percentage = total / 5

# print("Percentage =", percentage, "%")

# Area of Reactangele
# length = float(input("Enter length: "))
# breadth = float(input("Enter breadth: "))

# area = length * breadth

# print("Area of Rectangle =", area)

#  Quotient and Remainder
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# quotient = num1 // num2
# remainder = num1 % num2

# print("Quotient =", quotient)
# print("Remainder =", remainder)

# Calculate Simple Interest
# p = float(input("Enter Principal: "))
# t = float(input("Enter Time: "))
# r = float(input("Enter Rate: "))

# si = (p * t * r) / 100

# print("Simple Interest =", si)

# Calculate Compound Interest
# p = float(input("Enter Principal: "))
# t = float(input("Enter Time: "))
# r = float(input("Enter Rate: "))

# amount = p * ((1 + r / 100) ** t)
# ci = amount - p

# print("Compound Interest =", ci)

# Find Third Angle of Triangle
# angle1 = float(input("Enter first angle: "))
# angle2 = float(input("Enter second angle: "))

# angle3 = 180 - (angle1 + angle2)

# print("Third Angle =", angle3)

# Find Roots of a Quadratic Equation
# import math

# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))

# d = b**2 - 4*a*c

# if d > 0:
#     root1 = (-b + math.sqrt(d)) / (2*a)
#     root2 = (-b - math.sqrt(d)) / (2*a)
#     print("Roots are:", root1, root2)

# elif d == 0:
#     root = -b / (2*a)
#     print("Root is:", root)

# else:
#     print("Imaginary roots")

# 
# Area of Triangle
# base = float(input("Enter base: "))
# height = float(input("Enter height: "))

# area = 0.5 * base * height

# print("Area of Triangle =", area)

# Area of Equilateral Triangle
# import math

# side = float(input("Enter side: "))

# area = (math.sqrt(3) / 4) * side * side

# print("Area of Equilateral Triangle =", area)

# Area and Circumference of Circle
# import math

# radius = float(input("Enter radius: "))

# area = math.pi * radius * radius
# circumference = 2 * math.pi * radius

# print("Area =", area)
# print("Circumference =", circumference)

# Volume of Sphere
import math

radius = float(input("Enter radius: "))

volume = (4/3) * math.pi * radius**3

print("Volume of Sphere =", volume)