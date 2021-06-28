n=int(input())
level=list(int(input()) for i in range(n))
level.reverse()


dif=0
ans=0
for i in range(1,n):
    if level[i-1]<=level[i]:
        dif = level[i]-level[i-1]+1
        level[i]-=dif
        ans+=dif
print(ans)