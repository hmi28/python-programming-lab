n=int(input("Enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2==0:
            p=1
            q=0
        else:
            q=1
            p=0
        print(p,end="") if j%2==0 else print(q, end="")
    print()