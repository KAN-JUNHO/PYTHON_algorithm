n=int(input())
box=[list(map(int,input().split())) for i in range(n)]
print(box)
dp=[0]*(n+1)

for i in range(n-1,-1,-1):
    if box[i][0]+i<=n:
        dp[i]=max(dp[i+1],box[i][1]+dp[i+box[i][0]])
print(dp[0])