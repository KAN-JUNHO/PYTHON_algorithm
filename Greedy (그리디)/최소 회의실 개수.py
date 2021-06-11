n=int(input())
room=[]
for i in range(n):
    start,end=map(int,input().split())
    room.append([start,1])
    room.append([end,-1])

room.sort()
ans=0
temp=0
for i,j in room:
    temp+=j
    ans=max(temp,ans)

print(ans)