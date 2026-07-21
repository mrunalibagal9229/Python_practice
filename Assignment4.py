## print all even nubers until n
# n = int (input("Enter a number : "))
# for i in range(2,n+1,2):
#   print(i)

## print all odd numbers until n
# n=int(input("enter a number:"))
# for i in range (1,n+1,2):
#     print(i)

##print sum of series up to n
# n=int(input("enter a number:"))
# sum=0 
# for i in range (1,n+1):
#  sum+=i
#  print("sum=",sum)

##print factorial of a number
# n=int(input("Eenter a number:"))
# fact=1
# for i in range(1, n+1):
#  fact*=i
# print("factorial=",fact)

## print fibonacci series up to n terms
# n= int(input("enter number of  "))
# a=0
# b=1

# for i in range(n):
#     print(a,end="")
#     c=a+b
#     a=b
#     b=c

## check if a given number is prime or not
# n=int(input("Enter a nuber:"))
# count=0
# for i in range (1,n+1):
#     if n% i==o:
#         count+=1

#     if count==2:
#         print("prime Number")
#     else:
#         print("Not a prime Number")

## print all integers up to n that arent divisible by 2 and 3

# n=int(input("Enter a number:"))
# for i in range (1,n+1):
#     if i%2 !=0 and i%3 !=0:
#         print(i)

##find number divisible by 7 and multiple of 5 in a given range 
# start =int(input("Enter start:"))
# end = int(input("enter end:"))

# for i in range (start,end+1):
#    if i%7==0 and i %5==0:
#       print(i)/

##print all numbersin a range divisible by a given number
# start =int (input("enter a number:"))
# end  = int (input("enter a  end number:"))
# num = int (input("Enter divisor:"))
# for i in range (start,end +1):
#    if i % num==0:
#     print(i)

## check if a number is perfect number 
# n= int(input("Enter a number :"))
# sum=0
# for i in range (1,n):
#     if n %i ==0:
#         sum+=i

#     if sum ==n:
#         print("Perfect Number")
#     else:
#         print("Not a perfect Number")

## check if a number is strong number 
# n = int(input("Enter a number:"))
# temp =n
# sum=0
# while temp>0:
#     digit =temp%10
#     fact=1
#     for i in range (1,digit+1):
#         fact*=i
#         sum+=fact
#         temp//=10

#         if sum==n:
#             print("Strong Number")
#         else:
#             print("Not a Strong Number")

## check armstrong number
n=int(input("Enter a number:"))
temp = n 
digits = len(str(n))
sum=0

while temp>0:
    digit =temp%10
    sum += digit ** digits
    temp//=10
    if sum == n:
        print("Armstrong Number ")
    else:
        print("Not an Armstrong Number ")