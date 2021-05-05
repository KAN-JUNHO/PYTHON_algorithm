n=int(input())
nums=list(map(int,input().split()))
plus,minus,mul,div = map(int,input().split())
max_val,min_val=-1000000001,1000000001

def solve(plus,minus,mul,div,idx,hap):
    global max_val,min_val
    if len(nums)-1==idx:
        max_val=max(max_val,hap)
        min_val=min(min_val,hap)
        return
    if plus>0:
        solve(plus-1, minus, mul, div, idx+1,hap+nums[idx+1])
    if minus>0:
        solve(plus, minus-1, mul, div, idx+1,hap-nums[idx+1])
    if mul>0:
        solve(plus, minus, mul-1, div, idx+1,hap*nums[idx+1])
    if div>0:
        if hap!=0:
            solve(plus, minus, mul, div-1, idx+1,int(hap/nums[idx+1]))
        else:
            solve(plus, minus, mul, div - 1, idx + 1, 0)
solve(plus,minus,mul,div,0,nums[0])
print(int(max_val))
print(int(min_val))

