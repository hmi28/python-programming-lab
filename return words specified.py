li=list(map(str,input("enter space seperated elements").split()))
l=[]
x=""
k=int(input("enter length of words"))
for i in li:
    if len(i)==k:
        l.append(i)
for i in l:
    x+=i
    x+=' '
print(x)