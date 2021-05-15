n=int(input())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(n):
    a=int(input())
    if a==1:
        print(1)
    elif a==2:
        print(2)
    elif a==3:
        print(4)
    else:
        for j in range(4,a+1):
            dp[j]=dp[j-3]+dp[j-2]+dp[j-1]
        print(dp[a])