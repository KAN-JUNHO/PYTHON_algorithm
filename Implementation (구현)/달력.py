box=[0]*366
n=int(input())
for _ in range(n):
    start,end=map(int,input().split())
    for i in range(start,end+1):
        box[i]+=1
h=0
w=0
ans=0
for i in range(366):
    if box[i]!=0:
        h=max(h,box[i])
        w+=1
    else:
        ans+=h*w
        h=0
        w=0
ans+= h*w
print(ans)