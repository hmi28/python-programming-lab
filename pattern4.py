##*****
##*****
##*****
##*****
##*****
##     *****
##     *****
##     *****
##     *****
##     *****
##
n=int(input("Enter the number "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
for i in range(1,n+1):
    for k in range(1,n+1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()