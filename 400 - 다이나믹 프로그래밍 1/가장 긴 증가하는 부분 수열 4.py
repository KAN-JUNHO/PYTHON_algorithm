n=int(input())
a=list(map(int,input().split()))
dp=[1]*(n)

for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))
print(dp)
dp=dp.reverse()

answer=[]
#난중에 다시풀기
