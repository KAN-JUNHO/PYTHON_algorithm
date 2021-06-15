n,c=map(int,input().split())
m=int(input())
town=[list(map(int,input().split())) for i in range(m)]
town.sort(key=lambda x:x[1])

temp=[c]*n
ans=0
for start,end,weight in town:
    minNum=c
    for i in range(start,end):
        minNum=min(temp[i],minNum)
    minNum=min(minNum,weight)

    for i in range(start,end):
        temp[i]-=minNum
    ans+=minNum
print(ans)