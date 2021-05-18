n=int(input())
box=list(map(int,input().split()))
dp=box[:]
for i in range(1,n):
    for j in range(i):
        if box[i]>box[j]:
            dp[i]=max(dp[i],dp[j]+box[i])
print(max(dp))