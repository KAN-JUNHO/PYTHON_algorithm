n=int(input())
dp=[[1,0,0,0,0,0,0,0,0,0] for i in range(n+1)]


for i in range(len(dp)):
    for j in range(len(dp[0])):
        dp[i][j]=(dp[i-1][j]+dp[i][j-1])%10007

print(dp[-1][-1]%10007)
print(dp)