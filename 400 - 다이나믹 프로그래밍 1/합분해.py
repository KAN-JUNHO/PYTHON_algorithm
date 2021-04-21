n,k=map(int,input().split())
dp=[[0]*(n) for i in range(k)]
for i in range(n):
    dp[0][i]=1

for i in range(k):
    dp[i][0]=i+1

for i in range(1,k):
    for j in range(1,n):
        dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000000
print(dp[k-1][n-1]%1000000000)