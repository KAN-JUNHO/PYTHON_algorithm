import sys
n=int(input())
board=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
ans=[]
dp=[[0]*n for _ in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            break
        ny=i+board[i][j]
        nx=j+board[i][j]
        if 0<=ny<n:
            dp[ny][j]+=dp[i][j]
        if 0<=nx<n:
            dp[i][nx]+=dp[i][j]
print(dp[-1][-1])