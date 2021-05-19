t=int(input())
for _ in range(t):
    n=int(input())
    coin=list(map(int,input().split()))
    target=int(input())
    dp=[0]*(target+1)
    dp[0]=1

    for i in coin:
        for j in range(i,target+1):
            dp[j]+=dp[j-i]
    print(dp[target])