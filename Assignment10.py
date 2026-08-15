# sum of all element of a list 

# numbers = [10,20,30,40,50]
# total =0
# for num in numbers:
#     total +=num

# print("sum=",total)

# maximum and minimun element in a list 

# numbers=[25 ,10,53,5,60,]
# maximum = numbers[0]
# minimum = numbers[0]

# for num in numbers:
#     if num > maximum :
#         maximum =num
#     if num < minimum:
#         minimum =num  

# print("maximum =",maximum) 
# print("minimum=",minimum)     
     
# second largest element in the list

# number =[10,24,45,45,67,20]

# number =list(set(number))
# number.sort()

# print("second largest =",number[-2])

# Reverse the list

# numbers=[45,23,47,12,18]

# reverse_list = [ ::-1]

# print("reverse list =",reverse_list)


# check whether an element is present and count its occurrences

# number =[10,20,10,40,24,56]

# element = int(input("Enter an element:"))

# if element in number:
#     print("Element is present ")
#     print("It occurs",number.count(element),"times")

# else:
#     print("Element is not present")


# Remove duplicates from the list 

# number =[10,20,38,10,30,35,56]

# new_list = []
# for num in number:
#     if num not in new_list:
#         new_list.append(num)

# print("List after removing duplicates =",new_list)        

# Create a new list containing the cube of each number

# number =[1,2,3,4,5]
# cube_list=[]

# for num in number:
#     cube_list.append(num ** 3)

# print("cube list = ",cube_list)

# Create a duplicate of an existing list without pointing to the same list

# numbers=[12,34,28,34,46,12]

# duplicate = numbers.copy()

# print("original list =",numbers)
# print("Duplicates list=",duplicate)

# print ("Both are same object :",numbers is duplicate)

# Create seprate list of even and odd numbers

# numbers=[10 ,15,20,48,30,40]

# even_list=[]
# odd_list=[]

# for num in numbers:
#     if num % 2 ==0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)

# print("Even element =", even_list)
# print("Odd element= ",odd_list)


# Remove all occurrences of a given element

# numbers = [10, 20, 10, 30, 10, 40, 50]

# element = int(input("Enter element to remove: "))

# while element in numbers:
#     numbers.remove(element)

# print("List after removing element =", numbers)

# Print numbers divisible by both m and n

# numbers = [10, 12, 15, 20, 24, 30, 36, 40, 60]

# m = int(input("Enter m: "))
# n = int(input("Enter n: "))

# print("Numbers divisible by both", m, "and", n, ":")

# for num in numbers:
#     if num % m == 0 and num % n == 0:
#         print(num)

# Create three lists of numbers, squares and cubes

# numbers = [1, 2, 3, 4, 5]

# squares = []
# cubes = []

# for num in numbers:
#     squares.append(num ** 2)
#     cubes.append(num ** 3)

# print("Numbers =", numbers)
# print("Squares =", squares)
# print("Cubes =", cubes)

# Print list after removing even numbers

numbers = [10, 15, 20, 25, 30, 35, 40, 45]

new_list = []

for num in numbers:
    if num % 2 != 0:
        new_list.append(num)

print("List after removing even numbers =", new_list)