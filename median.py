n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))

if n1>n2 and n1<n3 or n1<n2 and n1>n3:
    print(n1)
elif n3>n2 and n3<n1 or n3<n2 and n3>n1:
    print(n3)
else:
    print(n2)