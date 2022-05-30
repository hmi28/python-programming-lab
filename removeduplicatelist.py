l=[]
size=int(input("Enter the size of the list"))
for i in range(size):
    ele=int(input())
    l.append(ele)
lis=[]
for i in range(0,size):
    flag=0
    for j in range(0,i):
        if l[i]==l[j]:
            flag=1
            break
    if flag==0:
        lis.append(l[i])
print(lis)