# li=[46,87,90,54,87,43]

# sum = 0

# for i in range(len(li)):
#     sum+= li[i]
# print(sum)

li=[46,87,90,54,87,43]

max = li[0]
for i in range(1,len(li)):
    if(li[i]>max):
        max=li[i]


print('maximun number:',max)