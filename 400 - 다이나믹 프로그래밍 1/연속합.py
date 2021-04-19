n=int(input())
box = list(map(int,input().split()))
dp=[0]*n

for i in range(n):
    dp[i]=max(box[i],dp[i-1]+box[i])

print(max(dp))
