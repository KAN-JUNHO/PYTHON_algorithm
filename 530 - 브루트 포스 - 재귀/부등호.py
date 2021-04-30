n=int(input())
box=list(map(str,input().split()))
check=[False]*10
min_val,max_val="10e9","0"
def dfs(pos, ans):
    global min_val,max_val
    if pos==n+1:
        min_val=min(min_val,ans)
        max_val=max(max_val,ans)
        return
    for i in range(10):
        if not check[i]:
            if pos==0 or eval(ans[-1]+box[pos-1]+str(i)):
                check[i]=True
                dfs(pos+1,ans+str(i))
                check[i]=False

dfs(0,"")
print(max_val)
print(min_val)