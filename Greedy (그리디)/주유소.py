n=int(input())
road=list(map(int,input().split()))
gas=list(map(int,input().split()))

v=gas[0]
ans=0
for i in range(n-1):
    if v>gas[i]:
        v=gas[i]
    ans+=v*road[i]

print(ans)