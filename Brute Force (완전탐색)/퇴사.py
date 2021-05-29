n=int(input())
dp=[0]*(n+1)
day=[0]*n
pay=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    day[i]=a
    pay[i]=b

for i in range(n):
    if dp[i]>dp[i+1]:
        dp[i+1]=dp[i]
    if i+day[i]<=n:
        dp[i+day[i]] = max(dp[i+day[i]],dp[i]+pay[i])
print(dp[n])