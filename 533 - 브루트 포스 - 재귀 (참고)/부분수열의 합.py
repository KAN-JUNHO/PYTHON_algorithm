from builtins import range

n=int(input())
nums=list(map(int,input().split()))
ans=[]
flag=[False]*(sum(nums)+2)
def dfs(idx,hap):
    if idx==n:
        flag[hap]=True
        return
    ans.append(hap+nums[idx])
    dfs(idx+1,hap+nums[idx])
    dfs(idx+1,hap)
dfs(0,0)
for i in range(len(flag)):
    if flag[i]==False:
        print(i)
        break