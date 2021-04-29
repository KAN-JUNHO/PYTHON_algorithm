n=int(input())
box=[]
for i in range(n):
    t,p=map(int,input().split())
    box.append([t,p])
dp=[0]*(n+1)

for i in range(n):
    dp[i]=max(dp[i],dp[i+1])
    dp[i+box[i][0]]=max(dp[i+box[i][0]],dp[i]+box[i][1])

print(dp[n])