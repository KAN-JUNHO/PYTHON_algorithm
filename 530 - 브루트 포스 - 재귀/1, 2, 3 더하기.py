t=int(input())
dp=[0]*11
dp[1]=1
dp[2]=2
dp[3]=4
dp[4]=7
for i in range(5,11):
    dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

for i in range(t):
    n=int(input())
    print(dp[n])
