import sys

n=int(sys.stdin.readline())
box=[]
for i in range(n):
    t,p=map(int,sys.stdin.readline().split())
    box.append([t,p])
dp=[0]*(n+max(box[0]))
for i in range(n):
    if i+box[i][0]<=n:
        dp[i+box[i][0]]=max(dp[i+box[i][0]],dp[i]+box[i][1])
    dp[i+1]=max(dp[i+1],dp[i])

print(max(dp))