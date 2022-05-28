n=int(input("Enter the number columnns"))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,n+1):
    for z in range(1,n+1):
        print(" ",end="")
    for k in range(i,n+1):
        print("*",end="")
    for j in range(1,i):
        print(" ",end="")
