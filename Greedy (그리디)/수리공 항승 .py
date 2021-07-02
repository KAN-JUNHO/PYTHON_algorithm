n,l=map(int,input().split())
box=list(map(int,input().split()))
box.sort()

temp=0
cnt=0
for i in box:
    if temp<i:
        cnt+=1
        temp = i + l -1
print(cnt)