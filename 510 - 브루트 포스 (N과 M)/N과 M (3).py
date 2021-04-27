n,m=map(int,input().split())
box=[]
def dfs(n,pos):
    if pos == m:
        print(*box)
        return
    for i in range(1,n+1):
        box.append(i)
        dfs(n,pos+1)
        box.pop()
dfs(n,0)