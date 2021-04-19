n=int(input())
dp=[0]
dp.append(1)
dp.append(1)
dp.append(2)
if n<4:
    print(dp[n])
else:
    for i in range(4,n+1):
        dp.append(dp[i-1]+dp[i-2])
    print(dp[-1])