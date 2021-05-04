n=int(input())
box=list(map(str,input().split()))
max_val="0"
min_val="10e9"
check =[False]*10
def solve(idx,ans):
    global max_val,min_val
    if idx==n+1:
        min_val = min(min_val, ans)
        max_val=max(max_val,ans)
        return
    for i in range(10):
        if not check[i]:
            if idx==0 or eval(ans[-1]+box[idx-1]+str(i)):
                check[i]=True
                solve(idx+1,ans+str(i))
                check[i]=False

solve(0,"")
print(max_val)
print(min_val)