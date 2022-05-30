lis_1=[]
size=int(input("Enter the size more than 5 elements of the list1"))
for i in range(size):
    ele=int(input())
    lis_1.append(ele)

rem=[]
for i in range(size):
    if i==0 or i==4 or i==5:
        pass
    else:
        rem.append(lis_1[i])
print(rem)