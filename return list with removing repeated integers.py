lis=list(map(int,input("enter space seperated elements").split()))
sil=lis
for i in lis:
    for j in lis:
        count=lis.count(i)
        if count>1:
            lis.remove(i)
print(lis)