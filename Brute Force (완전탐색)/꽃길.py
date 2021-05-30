n=int(input())
flowers=[list(map(int,input().split())) for i in range(n)]
check=[[False]*6 for i in range(n)]
cost=0
ans=10e9
dy = [1, 0, 0, 0, -1]
dx = [0, -1, 0, 1, 0]
def visited(y,x):
    for i in range(4):
        ndy=y+dy[i]
        ndx=y+dx[i]
        if 0<=ndy<n-1 and 0<=ndx<n-1 and not check[ndy][ndx]:
            pass
        else:
            return False
    else:
        return True
def cal(y,x):
    hap=0
    for i in range(4):
        ndy = y + dy[i]
        ndx = y + dx[i]
        hap+=flowers[ndy][ndx]
    return hap
def dfs(y,x,cost,cnt):
    global ans
    if cnt==3:
        ans=min(ans,cost)
        return

    for i in range(n):
        for j in range(n):
            if visited(i,j):
                for v in range(5):
                    check[i+dy[v]][i+dx[v]]=True
                dfs(i,j,cost+cal(i,j),cnt+1)
                for v in range(5):
                    check[i+dy[v]][i+dx[v]]=False

dfs(1,1,0,0)
print(cost)