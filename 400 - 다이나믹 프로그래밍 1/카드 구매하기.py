n=int(input())
cards=[0]+list(map(int,input().split()))
dp=[0]*(n+1)
dp[1]=cards[1]
dp[2]=max(cards[2],cards[1]*2)
for i in range(3,n+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i],dp[i-j]+cards[j])
print(dp)