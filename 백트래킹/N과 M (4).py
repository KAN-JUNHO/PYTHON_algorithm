n,m = map(int,input().split())
box=[]
check = [False]*n
def dfs(pos,x):
    if m==x:
        print(*box)
        return
    for i in range(pos,n+1):
        box.append(i)
        dfs(i,x+1)
        box.pop()
dfs(1,0)