import sys
n = int(sys.stdin.readline())
t,p,=[0]*n,[0]*n

for i in range(n):
    t[i],p[i] = list(map(int,sys.stdin.readline().split()))

dp =[0]*(n+1)
for i in range(n):
    if dp[i+1]<dp[i]:
        dp[i+1]=dp[i]
    if i+t[i]<=n:
        dp[i+t[i]] = max(dp[i]+p[i],dp[i+t[i]])

print(dp)