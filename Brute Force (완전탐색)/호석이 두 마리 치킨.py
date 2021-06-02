n,m=map(int,input().split())
cost=[[10e9]*n for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    cost[a-1][b-1]=1
    cost[b-1][a-1]=1
for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
print(cost)