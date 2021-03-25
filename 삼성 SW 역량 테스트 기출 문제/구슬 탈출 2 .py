import sys
from collections import deque
n,m = list(map(int,sys.stdin.readline().split()))
maps = [list(map(str,sys.stdin.readline())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == "R":
            maps[i][j]="."
            red = [i,j]
        elif maps[i][j] == "B":
            maps[i][j]="."
            blue = [i,j]


def movemove(y, x, dy, dx):
    move=0
    while maps[y+dy][x+dx] != "#":
        if maps[y+dy][x+dx] == "O":
            return 0, 0, 0
        x+=dx
        y+=dy
        move+=1
    return y,x,move

def dfs():
    visit={}
    visit[red[0],red[1],blue[0],blue[1]]=0
    que = deque([red+blue])
    while que:
        ry,rx,by,bx = que.popleft()
        for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
            rny,rnx,rmove = movemove(ry,rx,dy,dx)
            bny,bnx,bmove = movemove(by,bx,dy,dx)

            if not bnx and not bny:
                continue
            elif not rnx and not rny:
                print(visit)
                return
            elif rnx==bnx and bny==rny:
                if rmove > bmove:
                    rnx -= dx
                    rny -= dy
                else:
                    bnx-=dx
                    bny-=dy
            if (rny,rnx,bny,bnx) not in visit:
                visit[rny,rnx,bny,bnx]=visit[ry,rx,by,bx]+1

                print(visit[rny,rnx,bny,bnx])
                print(visit[ry,rx,by,bx])
                print()
                que.append((rny,rnx,bny,bnx))

dfs()
