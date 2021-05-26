n,m,r = map(int,input().split())
box=[list(map(int,input().split())) for i in range(n)]

for _ in range(r):
    for i in range(min(n,m)//2):
        x,y=i,i
        v=box[y][x]
        for j in range(i+1,n-i):
            y=j
            pre=box[j][x]
            box[j][x]=v
            v=pre
        for j in range(i+1,m-i):
            x=j
            pre=box[y][j]
            box[y][j]=v
            v=pre
        for j in range(i+1,n-i):
            y=n-j-1
            pre=box[n-j-1][x]
            box[n-j-1][x]=v
            v=pre
        for j in range(i+1,m-i):
            x=m-j-1
            pre=box[y][m-j-1]
            box[y][m-j-1]=v
            v=pre
for i in box:
    print(*i)