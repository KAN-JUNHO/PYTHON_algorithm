n=int(input())
#n 4
dp=[[0,0,0] for i in range(n)]
dp.insert(1,[1,1,1])
for i in range(2,n+1):
    dp[i][0]= (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%9901
    dp[i][1]= (dp[i-1][0]+dp[i-1][2])%9901
    dp[i][2]= (dp[i-1][0]+dp[i-1][1])%9901
print(sum(dp[-1])%9901)
