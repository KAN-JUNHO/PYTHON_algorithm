import sys
sys.setrecursionlimit(10000)
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
def dfs(y,x):
    land[y][x]="#"
    for i in range(8):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<h and 0<=nx<w and land[ny][nx]==1:
            dfs(ny,nx)
while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    land = [list(map(int,input().split())) for i in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if land[i][j]==1:
                dfs(i,j)
                cnt+=1

    print(cnt)
