arr=[[1,2,3],[4,5,6],[7,8,9]]
out=0
for i in range (len(arr)):
    for j in range (len(arr)):
        out[i][j]=arr[j][i]+out[i][j]
print(out)
