n= int(input())
room = [list(map(int,input().split())) for i in range(n)]
room.sort(key=lambda x:(x[1],x[0]))

end=0
ans=0
for i in range(n):
    if room[i][0]>=end:
        ans+=1
        end=room[i][1]
print(ans)
