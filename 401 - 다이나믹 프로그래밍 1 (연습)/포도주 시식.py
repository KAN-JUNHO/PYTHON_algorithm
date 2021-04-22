t=int(input())
wine=[]
for i in range(t):
    wine.append(int(input()))
wine.insert(0,0)

dp=[0]*(t+1)

if t>2:
    dp[1] = wine[1]
    dp[2] = dp[1] + wine[2]
    for i in range(3,t+1):
        dp[i]=max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])
    print(max(dp))
else:
    print(sum(wine))