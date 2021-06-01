n=int(input())
dy=[1,0,0,0,-1]
dx=[0,-1,0,1,0]
visited=[[False]*n for i in range(n)]
flowers=[list(map(int,input().split())) for i in range(n)]
ans=10e9
def check(y,x):
    for i in range(5):
        ndy=y+dy[i]
        ndx=x+dx[i]
        if ndy<0 or ndy>n-1 or ndx<0 or ndx>n-1 or visited[ndy][ndx]:
            return False
    return True
def cal(y,x):
    result=0
    for i in range(5):
        ndy=y+dy[i]
        ndx=x+dx[i]
        result+=flowers[ndy][ndx]
    return result
def dfs(y,cnt,hap):
    global ans
    if cnt==3:
        ans=min(ans,hap)
        return
    for i in range(y,n):
        for j in range(1,n):
            if check(i,j):
                for a in range(5):
                    visited[i+dy[a]][j+dx[a]] =True
                dfs(i,cnt+1,hap+cal(i,j))
                for a in range(5):
                    visited[i+dy[a]][j+dx[a]] =False


dfs(1,0,0)
print(ans)