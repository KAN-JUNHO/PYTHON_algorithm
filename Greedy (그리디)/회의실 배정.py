n=int(input())
room=[list(map(int,input().split())) for i in range(n)]

room.sort(key=lambda x : (x[1],x[0]))

start=room[0][0]
end=room[0][1]
cnt=1
for i in range(1,len(room)):
    if room[i][0] >= end:
        end=room[i][1]
        cnt+=1

print(cnt)
