n,m = map(int,input().split())
dots = [list(map(str,input())) for i in range(n)]
ans=False
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y,cnt):
    global pos_x,pos_y,ans
    if ans:
        return
    for i in range(4):
        ndy=dy[i]+y
        ndx=dx[i]+x
        if 0<=ndy<n and 0<=ndx<m:
            if not check[ndy][ndx] and dots[pos_y][pos_x]==dots[ndy][ndx]:
                check[ndy][ndx]=True
                dfs(ndy,ndx,cnt+1)
                check[ndy][ndx]=False
            elif cnt>=4 and ndx==pos_x and ndy==pos_y:
                ans=True
                return

game_over=False
for i in range(n):
    if game_over==True:
        break
    for j in range(m):
        pos_y = i
        pos_x = j
        check = [[False]*m for i in range(n)]
        check[i][j]=True
        dfs(j,i,1)
        if ans:
            print("YES")
            game_over=True
            break
else:
    print("NO")