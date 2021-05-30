n=int(input())
day=[]
pay=[]
for i in range(n):
    a,b=map(int,input().split())
    day.append(a)
    pay.append(b)
dp=[0]*(n+1)
for i in range(n):
    if dp[i]>dp[i+1]:
        dp[i+1]=dp[i]
    if i+day[i]<=n:
        dp[i+day[i]]=max(dp[i+day[i]],dp[i]+pay[i])
print(dp[n])