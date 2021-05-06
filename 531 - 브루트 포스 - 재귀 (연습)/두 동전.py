import collections
n,m=map(int,input().split())
board=[list(map(str,input())) for i in range(n)]

pos=[]
for i in range(n):
    for j in range(m):
        if board[i][j]=="o":
            pos.append([i,j])
coin=collections.deque()
coin.append([pos[0][0],pos[0][1],pos[1][0],pos[1][1],0])
y=[-1,1,0,0]
x=[0,0,-1,1]
check=False
cnt=0
while coin:
    if check==True:
        break
    ay,ax,by,bx,cnt = coin.popleft()
    if cnt>9:
        cnt=-1
        check=True

    for i in range(4):
        nay=ay+y[i]
        nax=ax+x[i]
        nby=by+y[i]
        nbx=bx+x[i]
        if 0<=nay<n and 0<=nax<m and 0<=nby<n and 0<=nbx<m:
            if board[nay][nax]=="#":
                nay=ay
                nax=ax
            if board[nby][nbx]=="#":
                nby=by
                nbx=bx
            coin.append([nay, nax, nby, nbx, cnt + 1])
        elif 0<=nay<n and 0<=nax<m:
            cnt+=1
            check=True
            break
        elif 0<=nby<n and 0<=nbx<m:
            cnt+=1
            check=True
            break

print(cnt)