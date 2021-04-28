n,m=map(int,input().split())
box=list(map(int,input().split()))
box.sort()
ans=[]
check=[True]*n
def dfs(pos):
    if len(ans)==m:
        print(*ans)
        return
    exist=0
    for i in range(pos,n):
        if check[i] and exist!=box[i]:
            exist=box[i]
            ans.append(box[i])
            check[i]=False
            dfs(i+1)
            check[i]=True
            ans.pop()
dfs(0)

