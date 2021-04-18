n=int(input())
cards = [0]+list(map(int,input().split()))
dp=[10000]*(n+1)
dp[0]=0
dp[1]=cards[1]
dp[2]=min(cards[1]*2,cards[2])
for i in range(3,n+1):
    for j in range(1,i+1):
        dp[i]=min(dp[i],dp[i-j]+cards[j])
print(dp[-1])