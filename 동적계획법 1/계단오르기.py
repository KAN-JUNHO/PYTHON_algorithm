n = int(input())
stair =[int(input()) for i in range(n)]
stair.insert(0,0)
print(stair)
dp=[0]*(n+1)
dp[1]=stair[1]
for i in range(2,n+1):
    dp[i]=max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i])
print(dp)