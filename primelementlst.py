print("Enter the size of the elements")
n=int(input())
l=[]
print("Enter the elements")
for i in range(0,n):
    element=int(input())
    l.append(element)
    
for i in range(0,n):
    temp=l[i]
    lis=[]
    flag=0
    for j in range(1,(temp+1)//2):
        if i%j==0:
            flag=1
    if flag==1:
        lis.append(l[i])
print("The required list is :",lis)