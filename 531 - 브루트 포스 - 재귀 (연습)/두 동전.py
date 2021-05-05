import collections
n,m=map(int,input().split())
board=[list(map(str,input())) for i in range(n)]
pos=[]
for i in range(n):
    for j in range(m):
        if board[i][j]=="o":
            pos.append([i,j])
            board[i][j]="."
dy=[1,0,-1,0]
dx=[0,1,0,-1]
def bfs():
    while coin:

        ay,ax,by,bx,cnt = coin.popleft()
        if cnt>9:
            return -1
        for i in range(4):
            nay=ay+dy[i]
            nax=ax+dx[i]
            nby=by+dy[i]
            nbx=bx+dx[i]
            if 0<=nay<n and 0<=nax<m and 0<=nby<n and 0<=nbx<m:
                if board[nay][nax]=="#":
                    nay=ay
                    nax=ax
                if board[nby][nbx]=="#":
                    nby=by
                    nbx=bx
                coin.append([nay,nax,nby,nbx,cnt+1])
            elif 0<=nay<n and 0<=nax<m:
                return cnt+1
            elif 0<=nby<n and 0<=nbx<m:
                return cnt+1
coin = collections.deque()
coin.append([pos[0][0],pos[0][1],pos[1][0],pos[1][1],0])
print(bfs())