n,m=map(int,input().split())
box=list(map(int,input().split()))
box.sort()
ans=[]
def dfs(n,pos,index):
    if pos==m:
        print(*ans)
        return
    for i in range(index,len(box)):
        ans.append(box[i])
        dfs(n,pos+1,i+1)
        ans.pop()

dfs(n,0,0)