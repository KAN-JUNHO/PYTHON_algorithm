n,k=map(int,input().split())
box=[]
for i in range(n):
    v,w=map(int,input().split())
    box.append([v,w])
box.insert(0,[0,0])
dp=[[0]*(k+1) for i in range(n+1)]
print(box)
for i in range(n+1):
    for j in range(k+1):
        if j>=box[i][0]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-box[i][0]]+box[i][1])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n-1][k-1])
