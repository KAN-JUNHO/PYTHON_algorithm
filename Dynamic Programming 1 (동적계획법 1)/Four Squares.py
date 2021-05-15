n=int(input())
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    val=10e9
    j=1
    while j**2<=i:
        val = min(val,dp[i-j**2]+1)
        j+=1
    dp[i]=val
print(dp[-1])