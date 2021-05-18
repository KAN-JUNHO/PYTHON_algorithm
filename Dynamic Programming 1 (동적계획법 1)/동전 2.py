n,k=map(int,input().split())
coin = [int(input()) for i in range(n)]
dp=[10e9]*(k+1)
dp[0]=0
for i in coin:
    for j in range(i,k+1):
        dp[j]=min(dp[j-i]+1,dp[j])
if dp[-1]==10e9:
    print(-1)
else:
    print(dp[-1])