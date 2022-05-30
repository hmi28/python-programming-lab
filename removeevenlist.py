lis_1=[]
size=int(input("Enter the size of the list1"))
for i in range(size):
    ele=int(input())
    lis_1.append(ele)
print()
for i in lis_1:
    if i%2!=0:
        print(i,end=" ")