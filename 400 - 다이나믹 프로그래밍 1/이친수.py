n=int(input())
dp=[0]
dp.append(1)
dp.append(1)
dp.append(2)
dp.append(3)

if n>4:
    for i in range(5,n+1):
        dp.append(dp[i-1]+dp[i-2])
    print(dp[-1])
else:
    print(dp[n])