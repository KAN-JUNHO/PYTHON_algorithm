n,m=map(int,input().split())
box=list(map(int,input().split()))
box.sort()
ans=[]
check=[True]*n
def dfs():
    if m==len(ans):
        print(*ans)
        return
    exist=0
    for i in range(n):
        if exist!=box[i] and check[i]:
            exist=box[i]
            ans.append(box[i])
            check[i]=False
            dfs()
            check[i]=True
            ans.pop()

dfs()
