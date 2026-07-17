# sum of frist 3 numbers
# sum = 0

# for i in range(1, 11):
#     sum += i

# print("Sum =", sum)


## Multiplication table
# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


## Factorial number
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)