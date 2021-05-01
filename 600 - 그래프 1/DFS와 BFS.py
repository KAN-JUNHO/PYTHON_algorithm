n,m,v =map(int,input().split())
graph = [[0] * (n+1) for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1
check=[0]*(n+1)

answer_dfs=[]
answer_bfs=[]
def dfs(v):
    check[v]=1
    answer_dfs.append(v)
    for i in range(1,n+1):
        if check[i]==0 and graph[v][i]==1:
            dfs(i)

def bfs(v):
    que = [v]
    check[v]=1
    while que:
        v=que.pop(0)
        answer_bfs.append(v)
        for i in range(1,n+1):
            if check[i]==0 and graph[v][i]==1:
                que.append(i)
                check[i]=1
dfs(v)
bfs(v)
print(*answer_dfs)
print(*answer_bfs)
