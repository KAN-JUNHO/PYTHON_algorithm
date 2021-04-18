import sys
m=int(sys.stdin.readline())
dp=[0]*(11)
dp[1]=1
dp[2]=2
dp[3]=4
for j in range(4, 11):
    dp[j] = dp[j - 3] + dp[j - 2] + dp[j - 1]
for i in range(m):
    n=int(sys.stdin.readline())
    print(dp[n])

