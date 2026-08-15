# put  Even and odd element of a list into two diffrent list

# number =[10,20,30,40,50,55]

# even =[]
# odd =[]

# for num in number:
#     if num %2==0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even element:",even)
# print("Odd element:",odd)

# Merge two lists and sort it

# list1 = [10,30,20,50]
# list2 = [40,70,40,49]

# merged_list = list1 + list2
# merged_list.sort()

# print("Merged and sorted list:",merged_list)

   
# sort the listaccording to the second element in sublist/

# numbers =[[1,2],[2,2],[3,8],[4,1],[5,6]]

# numbers.sort(key=lambda x: x[1])
# print("list sorted according to second element:")
# print(numbers)


# find the second largest number using bubble sort 

# numbers=[20,30,12,49,45,67,78]

# for i in range (len(numbers)):
#     for j in range (0,len(numbers) -i -1):
#         if numbers[j]>numbers[i+1]:
#             numbers[j],numbers[j+1]=numbers[j+1],numbers[j]


# print("sorted list:",numbers)
# print("second largest number:",numbers[-2])


# sort a list according to the length of elements 

# word=["apple","mouse","dog","pen","rat"]

# word.sort(key=len)

# print("list sorted according to lenth:")
# print(word)

# find the of two lists 

# list1=[1,2,3,4,5]
# list2=[4,5,6,7,1]

# union=list(set(list1)|set(list2))

# print("union of two lists:",union)

# find the insection of two lists

# list1=[1,2,2,3,4,5]
# list2=[4,5,5,6,7,8]

# intersection=list(set(list1)&set(list2))

# print("Intersection of two lists:",intersection)


# print 1 to 100  snske and ladder pattern

# for row in range (10):
#     start =row * 10 + 1
#     end =start +10

#     numbers =list(range (start ,end))
#     if row % 2 !=0:
#         numbers.reverse()

#         print(*numbers) 

# Create three list of numbers,squares and cubes

# numbers =[1,2,3,4,5]
# squares =[]
# cubes =[]

# for num in numbers:
#     squares.append(num**2)
#     cubes.append(num ** 3)

# print("Numbers: ",numbers) 
# print("Squares:",squares)
# print("cubes:",cubes)


# print list after removing even numbers

# numbers=[110,23,10,15,25,28,45,30]

# odd_numbers=[]

# for num in numbers:
#     if num % 2 !=0:
#         odd_numbers.append(num)

# print("List after removing even numbers :",odd_numbers)        


