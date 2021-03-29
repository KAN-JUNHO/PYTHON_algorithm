import collections
n,m = map(int,input().split())
box=[]
for i in range(n):
    arr = str(input())
    box.append(arr)
val=float("INF")
ans=[]
for i in range(n-7):
    for j in range(m-7):
        cnt1=0
        cnt2=0
        for y in range(i,i+8):
            for x in range(j,j+8):
                if (x+y)%2==0:
                    if box[y][x] != "W":
                        cnt1+=1
                    if box[y][x] != "B":
                        cnt2+=1
                else:
                    if box[y][x] !="B":
                        cnt1+=1
                    if box[y][x] !="W":
                        cnt2+=1
        ans.append(cnt1)
        ans.append(cnt2)

print(min(ans))