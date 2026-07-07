# # 1.structure : denoted by []
# li =[10,20,40,"pqr"]

# # 2. types of data: Hetrogeneous

# # 3. sequence : orderd 

# # 4. changable:

# print(id(li))
# li[0]=40
# print(id(li))
# print(li)

# # 5. Duplication :allowed
# li=[10,20,10,20,30,30]
# print(li)

# li=["apple","banana","cheri","mango"]
# print(li)

# list of numbers and print frist ,last,thrid element.

# li=[20,10,34,24,25,78,45,65,45,20]
# print(li[0])
# print(li[9])
# print(li[2])

# li=[10,20,30.40,50]
# li[2]=300
# print(li)

# Revers element list
# li=[20,10,60,45,20,45,10,10]
# # print(li.count)
# # print(li[::-1])
# # slicing 
# print(li[3:-2])

# print each element sepratly
# li= [20,"pqr",1.3,"true","false"]
# for i in li:
#     print(i)

# list of 5 numbers find and print sum of all elements

# li=[3,5,4,8,9,6]
# print(li)
# sum=0
# for i in li:
#     sum+=i
# print(sum)

# LARGEST AND 2ND LARGEST ELEMENT

li=[20,80,35,36,67,87 ,56]
li=list(set(li))
li.sort()

print("Largest:",li[-1])
print("2nd Largest",li[-2])