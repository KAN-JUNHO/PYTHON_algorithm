n = int(input())
nums = list(map(int,input().split()))
plus,minus,mul,div= (map(int,input().split()))

max_,min_ = 1e9,1e9

def dfs(i, pos, plus, minus, mul, div):
    global max_,min_
    if i==n:
        max_=max(max_,pos)
        min_=min(min_,pos)
        return
    else:
        if plus>0:
            dfs(i+1, pos+nums[i], plus-1, minus, mul, div)
        if minus>0:
            dfs(i+1, pos-nums[i], plus, minus-1, mul, div)
        if mul>0:
            dfs(i+1, pos*nums[i], plus, minus, mul-1, div)
        if div>0:
            dfs(i+1, int(pos/nums[i]), plus, minus, mul, div-1)
dfs(1,nums[0],plus,minus,mul,div)
print(max_)
print(min_)