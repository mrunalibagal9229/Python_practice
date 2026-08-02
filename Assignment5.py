# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


# correct_userid = "admin"
# correct_password = "1234"

# for attempt in range(3):
#     userid = input("Enter User ID: ")
#     password = input("Enter Password: ")

#     if userid == correct_userid and password == correct_password:
#         print("Login Successful!")
#         break
#     else:
#         print("Invalid User ID or Password.")
# else:
#     print("Maximum attempts reached. Program terminated.")

# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.


# # Enter number of students
# n = int(input("Enter number of students: "))

# total_percentage = 0

# for i in range(1, n + 1):
#     print(f"\nEnter marks of 5 subjects for Student {i}:")
    
#     total_marks = 0

#     for j in range(1, 6):
#         marks = float(input(f"Subject {j} marks: "))
#         total_marks += marks

#     percentage = (total_marks / 500) * 100
#     total_percentage += percentage

#     print(f"Percentage of Student {i}: {percentage:.2f}%")

# # Calculate average percentage of all students
# average_percentage = total_percentage / n

# print("\n----- Result -----")
# print(f"Average Percentage of all Students: {average_percentage:.2f}%")


# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.



# # Accept number of passengers and ticket cost
# n = int(input("Enter number of passengers: "))
# ticket_cost = float(input("Enter ticket cost: "))

# total_amount = 0

# for i in range(1, n + 1):
#     age = int(input(f"Enter age of Passenger {i}: "))

#     if age < 12:
#         amount = ticket_cost - (ticket_cost * 0.30)   # 30% discount
#     elif age > 59:
#         amount = ticket_cost - (ticket_cost * 0.50)   # 50% discount
#     else:
#         amount = ticket_cost                          # Full fare

#     total_amount += amount

# print("\nTotal Ticket Amount =", total_amount)


# WAP to print Armstrong number within a given range

# # Armstrong numbers in a given range

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# print("Armstrong numbers are:")

# for num in range(start, end + 1):
#     temp = num
#     digits = len(str(num))
#     total = 0

#     while temp > 0:
#         digit = temp % 10
#         total += digit ** digits
#         temp //= 10

#     if total == num:
#         print(num)

#         Write a program to print prime numbers between 1 to 100.

#         n = int(input("Enter the value of n: "))

# count = 0
# num = 2

# print("First", n, "prime numbers are:")

# while count < n:
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num, end=" ")
#         count += 1

#     num += 1


#     Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

#  1)n = int(input("Enter n: "))

# fact = 1
# sum = 0

# for i in range(1, n + 1):
#     fact *= i
#     sum += fact

# print("Sum =", sum)

#  2)n = int(input("Enter N: "))

# sum = 0

# for i in range(1, n + 1):
#     sum += n ** i

# print("Sum =", sum)

# 3)n = int(input("Enter number of terms: "))

# sum = 0
# term = 1

# for i in range(n):
#     sum += term
#     term *= 2

# print("Sum =", sum)

# 4)a = int(input("Enter value of a: "))

# sum = 0

# for i in range(1, 11):
#     sum += (a ** i) / i

# print("Sum =", sum)

# 5)x = int(input("Enter value of x: "))
# n = int(input("Enter number of terms: "))

# sum = 0
# sign = 1
# denominator = 1

# for i in range(1, n + 1):
#     sum += sign * (x ** i) / denominator
#     sign *= -1
#     denominator += 2

# print("Sum =", sum)