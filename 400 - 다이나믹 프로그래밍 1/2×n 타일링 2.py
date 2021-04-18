n=int(input())
dp=(n+1)*[0]
if n<2:
    print(n)

else:
    dp[1]=1
    dp[2]=3
    for i in range(3,n+1):
        dp[i]=(dp[i-2]*2)+dp[i-1]
    print(dp[-1]%10007)