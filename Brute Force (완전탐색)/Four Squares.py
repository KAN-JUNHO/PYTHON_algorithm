dp=[0 for i in range(50001)]
n=int(input())
dp[1]=1
for i in range(2,n+1):
    j=1
    val=10e9
    while j**2<=i:
        val=min(val,dp[i-j**2]+1)
        j+=1
    dp[i]=val
print(dp[n])