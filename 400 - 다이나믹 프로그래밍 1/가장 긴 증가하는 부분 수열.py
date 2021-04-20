import bisect
n=int(input())
a=list(map(int,input().split()))
dp=[a[0]]
for i in range(n):
    if a[i]>dp[-1]:
        dp.append(a[i])
    else:
        idx = bisect.bisect_left(dp,a[i])
        dp[idx]=a[i]
print(dp)

#7
#10 30 20 50 40 90 60