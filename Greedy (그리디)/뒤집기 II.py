n,m=map(int,input().split())
maps=[list(map(int,input())) for i in range(n)]

def revesre(y,x):
    for i in range(0,y+1):
        for j in range(0,x+1):
            maps[i][j]=1-maps[i][j]


cnt=0
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if maps[i][j]==1:
            cnt+=1
            revesre(i,j)

print(cnt)