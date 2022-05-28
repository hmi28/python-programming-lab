##     *
##    ***
##   *****
##    ***
##     *
##

n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end="")
    for k in range(2,i+1):
        print("*",end="")
    for k in range(2,i):
        print("*",end="")
    print()

for i in range(2,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(i,n):
        print("*",end="")
    for k in range(i+1,n):
        print("*",end="")
    print()