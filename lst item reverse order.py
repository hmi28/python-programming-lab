size=int(input("Enter the size of the both list"))
ls_1=[]
print("Enter the first list element")
for i in range(0,size):
    ele=input()
    ls_1.append(ele)
    
ls_2=[]
print("Enter the second list element")

for i in range(0,size):
    ele=input()
    ls_2.append(ele)


for i in range(0,size):
    print(ls_1[i],ls_2[size-1-i],end=" ",sep=",")
    