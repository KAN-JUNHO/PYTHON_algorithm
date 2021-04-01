n,m = map(int,input().split())
box=[]
def dfs(x):
    if m==x:
        print(*box)
        return
    for i in range(1,n+1):
        box.append(i)
        dfs(x+1)
        box.pop()

dfs(0)