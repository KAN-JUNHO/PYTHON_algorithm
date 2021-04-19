n=int(input())
dp=[0]*(n+1)

for i in range(1,n+1):
    dp[i]=i
    for j in range(1,i):
        if i<j**2:
            break
        dp[i]=min(dp[i],dp[i-j**2]+1)
print(dp)