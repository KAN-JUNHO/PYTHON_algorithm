import collections
m,n=map(int,input().split())
tomato = [list(map(int,input().split())) for i in range(n)]
que = collections.deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            que.append([i,j])
dx=[0,0,-1,1]
dy=[-1,1,0,0]
cnt=0
while que:
    y,x = que.popleft()
    for i in range(4):
        ndy=dy[i]+y
        ndx=dx[i]+x
        if 0<=ndy<n and 0<=ndx<m:
            if tomato[ndy][ndx]==0:
                tomato[ndy][ndx]=tomato[y][x]+1
                que.append([ndy,ndx])
ans=[]
for i in tomato:
    if 0 in i:
        print(-1)
        break
    else:
        ans.append(max(i))
else:
    print(max(ans)-1)
