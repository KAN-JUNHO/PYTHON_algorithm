n=int(input())

box = [list(map(int,input().split())) for i in range(n)]
check = [False]*n
print(box)
ans=0
def dfs(idx,cnt):
    global ans
    if cnt==n//2:
        start,link=0,0
        for i in range(n):
            for j in range(n):
                if check[i] and check[j] and i!=j:
                    start+=box[i][j]
                elif not check[i] and not check[j] and i!=j:
                    link+=box[i][j]
        ans=min(ans,abs(start-link))

    for i in range(idx,n):
        check[i]=True
        dfs(idx+1,cnt+1)
        check[i]=False

dfs(0,0)
print(ans)