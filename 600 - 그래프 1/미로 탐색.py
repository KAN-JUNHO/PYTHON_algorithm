import collections
import sys
h,w=map(int,sys.stdin.readline().split())
miro = [list(map(int,sys.stdin.readline().strip())) for i in range(h)]
check =[[0]*w for _ in range(h)]
check[0][0]=1
dy=[1,-1,0,0]
dx=[0,0,-1,1]
que=collections.deque([[0, 0]])
while que:
    y,x=que.popleft()
    if y==h-1 and x==w-1:
        print(check[y][x])
        break
    for i in range(4):
        ndy = dy[i]+y
        ndx = dx[i]+x
        if 0<=ndy<h and 0<=ndx<w and check[ndy][ndx]==0 and miro[ndy][ndx]==1:
            check[ndy][ndx] = check[y][x]+1
            que.append([ndy,ndx])