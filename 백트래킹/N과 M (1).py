n,m = map(int,input().split())
cnt=0
box=[]
def dfs(x):
    if x == m:
        print(*box)
        return
    for i in range(1,n+1):
        if i in box:
            continue
        box.append(i)
        dfs(x+1)
        box.pop()
dfs(0)