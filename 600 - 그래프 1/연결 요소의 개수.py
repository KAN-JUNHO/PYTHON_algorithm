n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
check=[False]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1
def dfs(v):
    check[v]=True
    for i in range(1,n+1):
        if check[i]==False and graph[v][i]==1:
            dfs(i)
cnt=0
for i in range(1,n+1):
    if check[i]==False:
        dfs(i)
        cnt+=1
print(cnt)