n= int(input())
nums=list(map(int,input().split()))
dp=[0]*n
for i in range(n):
    dp[i]=max(dp[i-1]+nums[i],nums[i])
print(max(dp))