a=int(input())
box=list(map(int,input().split()))
plus,minus,mul,div=map(int,input().split())
max_val,min_val=-1000000001,1000000001

def dfs(plus,minus,mul,div,idx,hap):
    global max_val,min_val
    if idx==len(box)-1:
        max_val=max(hap,max_val)
        min_val=min(hap,min_val)
        return
    if plus>0:
        dfs(plus-1,minus,mul,div,idx+1,hap+ box[idx+1])
    if minus>0:
        dfs(plus,minus-1,mul,div,idx+1,hap - box[idx+1])
    if mul>0:
        dfs(plus,minus,mul-1,div,idx+1,hap * box[idx+1])
    if div>0:
        if hap!=0:
            dfs(plus,minus,mul,div-1,idx+1,int(hap / box[idx+1]))
        else:
            dfs(plus, minus, mul, div - 1, idx + 1, 0)



dfs(plus,minus,mul,div,0,box[0])
print(max_val)
print(min_val)