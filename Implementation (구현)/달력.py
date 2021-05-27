box=[0]*366
n=int(input())
for _ in range(n):
    start,end=map(int,input().split())
    for i in range(start,end+1):
        box[i]+=1
h=0
w=0
hap=0
for i in range(366):
    if box[i]==0:
        hap+=w*h
        w=h=0
    else:
        h=max(h,box[i])
        w+=1
hap+=h*w
print(hap)