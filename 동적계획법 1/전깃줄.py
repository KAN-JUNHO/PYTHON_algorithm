n=int(input())
box =[list(map(int,input().split())) for i in range(n)]
box.sort()
print(box)

dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if box[i][1] > box[j][1]:
            dp[i]= max(dp[i],dp[j]+1)

print(n-max(dp))