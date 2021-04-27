n,m=map(int,input().split())
box=[]

def dfs(index,pos):
    if pos==m:
        print(*box)
        return
    for i in range(index,n+1):
        box.append(i)
        dfs(index,pos+1)
        index+=1
        box.pop()


dfs(1,0)