##9)  write a program in python input a number find that number is square root , square , cube or cube root

num=int(input("Enter the number"))
print("THE square of the number is ",num*num)
print("The cube of the number is ",num*num*num)
flag=0
for i in range(1,num+1):
        if num==(i*i):
            print("The square root is " , i)
            flag=1
            break
if flag==0:
    print("The square root of the number is not find")
flag=0
for i in range(1,num+1):
        if num==(i*i*i):
            flag=1
            print("The cube of the number is ", i)
            break
if flag==0:
    print("The cube root of the number is not find")