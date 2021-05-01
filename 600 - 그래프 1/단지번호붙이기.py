n=int(input())
box=[list(map(int,input())) for i in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=[]
def dfs(x,y):
    global num
    box[y][x]="#"
    num += 1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and box[ny][nx]==1:
            dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if box[i][j]==1:
            num = 0
            dfs(j,i)
            ans.append(num)

print(len(ans))
ans.sort()
for i in ans:
    print(i)