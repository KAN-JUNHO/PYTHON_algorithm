n=int(input())
a=list(map(int,input().split()))
dp=a[:]
for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i]=max(dp[i],dp[j]+a[i])
print(max(dp))