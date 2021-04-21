import sys
n=int(sys.stdin.readline())
dp=[i for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i):
        if i<j*j:
            break
        dp[i]=min(dp[i],dp[i-j*j]+1)

print(dp[n])
