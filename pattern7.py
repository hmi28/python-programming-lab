##7) Write a python program to print a following pattern
##
##
##           *
##          ***
##         *****
##        *******
##
##

n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    for k in range(1,i):
        print("*",end="")
    print()