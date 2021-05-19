n=int(input())
box=[[0]*10 for _ in range(n)]
box.insert(0,[0,1,1,1,1,1,1,1,1,1])

for i in range(1,n):
    for j in range(10):
        if j==0:
            box[i][j] = box[i-1][j+1]
        elif j==9:
            box[i][j] = box[i-1][j-1]
        else:
            box[i][j]=box[i-1][j-1]+box[i-1][j+1]
print(sum(box[n-1])%1000000000)