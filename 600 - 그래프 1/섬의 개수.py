import sys
sys.setrecursionlimit(100000)
def dfs(x,y):
    land[y][x]="#"

    for i in range(8):
        ndy=dy[i]+y
        ndx=dx[i]+x
        if 0<=ndy<h and 0<=ndx<w and land[ndy][ndx]==1:
            dfs(ndx,ndy)

while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    land = [list(map(int,input().split())) for i in range(h)]
    dx=[-1,0,1,-1,1,-1,0,1]
    dy=[-1,-1,-1,0,0,1,1,1]
    cnt=0
    for i in range(h):
        for j in range(w):
            if land[i][j]==1:
                dfs(j,i)
                cnt+=1


    print(cnt)