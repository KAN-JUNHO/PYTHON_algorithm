n=int(input())
nums=list(map(int,input().split()))
dp=[0]*(n+1)
dp[0]=nums[0]
for i in range(1,n):
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i]=max(dp[i],dp[j]+nums[i])
print(max(dp))