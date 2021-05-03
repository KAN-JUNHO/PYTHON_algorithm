t=int(input())
def dfs(x,cnt):
    if check[x]:
        if cnt-dist[x]>=3:
           return x
        else:
            return -1
    check[x]=1
    dist[x]=cnt
    for i in station[x]:
        cycle = dfs(i,cnt+1)
        if cycle != -1:
            check[x]=2
            if x==cycle:
                return -1

    return -1


station = [[] * (t+1)for i in range(t+1)]
check = [0] * (t + 1)
dist = [0] * (t + 1)
for i in range(t):
    u, v = map(int, input().split())
    station[v].append(u)
    station[u].append(v)
print(station)
dfs(1,0)
print(check)