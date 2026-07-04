a, b, c = [10,12,13]

print(a)
print(b)
print(c)


numbers = 10, 12, 13
print(numbers)
print(type(numbers))

# packing - Packing means combining multiple values into a single variable (usually a tuple).
# Combines multiple values into one variable


# unpacking - Unpacking means extracting values from a list, tuple, or other iterable into multiple variables.
# Splits one iterable into multiple variables

name, age, course = ("Ram", 22, "Python")

print(name)
print(age)
print(course)


a, *b = [10, 20, 30, 40]
print(a)
print(b)



a, *b, c = [10, 20, 30, 40, 50]

print(a)
print(b)
print(c)