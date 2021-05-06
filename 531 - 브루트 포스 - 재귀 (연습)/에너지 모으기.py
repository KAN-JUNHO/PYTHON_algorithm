n=int(input())
box=list(map(int,input().split()))
ans=0
def dfs(hap):
    global ans
    if len(box)==2:
        ans=max(hap,ans)
        return
    for i in range(1,len(box)-1):
        v = box[i-1]*box[i+1]
        temp=box[i]
        del box[i]
        dfs(hap+v)
        box.insert(i,temp)

dfs(0)
print(ans)