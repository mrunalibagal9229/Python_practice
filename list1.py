def createlist(li):
    n = int(input('How many elements you wantadd:'))
    for i in range(n):
        ele = int(input('enter element:'))
        li.append(ele)

li=[]
createlist(li)
print(li)
