n,m=map(int,input().split())
box=list(map(int,input().split()))
box.sort()
ans=[]
def dfs(pos):
    if m==pos:
        print(*ans)
        return
    for i in box:
        ans.append(i)
        dfs(pos+1)
        ans.pop()
dfs(0)