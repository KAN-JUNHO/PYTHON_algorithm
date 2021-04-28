n,m=map(int,input().split())
box=list(map(int,input().split()))
box.sort()
ans=[]
def dfs(pos):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(pos,len(box)):
        ans.append(box[i])
        dfs(pos)
        pos+=1
        ans.pop()

dfs(0)