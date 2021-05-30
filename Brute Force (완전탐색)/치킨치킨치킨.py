n,m=map(int,input().split())
chicken = [list(map(int,input().split())) for i in range(n)]
visited =[False]*m
cnt=0
ans=0
def dfs(start,depth):
    global ans
    if depth==3:
        hap=0
        for i in range(n):
            temp=0
            for j in range(m):
                if visited[j]:
                    temp=max(temp,chicken[i][j])
            hap+=temp
        ans=max(ans,hap)
        return

    for i in range(start,m):
        if not visited[i]:
            visited[i]=True
            dfs(i,depth+1)
            visited[i]=False
dfs(0,0)

print(ans)