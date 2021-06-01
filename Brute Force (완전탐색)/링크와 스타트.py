n=int(input())
box = [list(map(int,input().split())) for i in range(n)]
check=[False]*n
ans=10e9

def dfs(pos,cnt):
    global ans
    if cnt==n//2:
        start,link=0,0
        for i in range(n):
            for j in range(n):
                if check[i] and check[j]:
                    start+=box[i][j]
                elif not check[i] and not check[j]:
                    link+=box[i][j]
        ans=min(ans,abs(start-link))

    for j in range(pos,n):
        if not check[j]:
            check[j]=True
            dfs(j+1,cnt+1)
            check[j]=False
dfs(0,0)
print(ans)