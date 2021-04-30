n=int(input())
box=[list(map(int,input().split())) for i in range(n)]
check=[False]*n
ans=10e9
def dfs(pos):
    global ans
    if n//2==check.count(True):
        start,link=0,0
        for i in range(n):
            for j in range(n):
                if check[i] and check[j]:
                    start+=box[i][j]
                elif not check[i] and not check[j]:
                    link+=box[i][j]
        ans = min(ans,abs(start-link))

    for i in range(pos,n):
        if not check[i]:
            check[i]=True
            dfs(i+1)
            check[i]=False

dfs(0)
print(ans)