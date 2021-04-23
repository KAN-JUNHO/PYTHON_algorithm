n=int(input())
a=list(map(int,input().split()))
dp=[[0]*n for i in range(2)]
dp[0][0]=a[0]

if n>1:
    answer = -10e9
    for i in range(1,n):
        dp[0][i]=max(dp[0][i-1]+a[i],a[i])
        dp[1][i]=max(dp[0][i-1],dp[1][i-1]+a[i])
        answer = max(dp[0][i],dp[1][i],answer)
    print(answer)

else:
    print(a[0])