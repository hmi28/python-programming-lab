num=int(input("Enter the number"))
flag=0
for i in range(1,num+1):
        if num==(i*i):
            print("Yes it is a perfect square number")
            flag=1
            break
if flag==0:
    print("No it is not a perfect square number")