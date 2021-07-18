from collections import deque
n,m=map(int,input().split())
cakes=list(map(int,input().split()))
cakes.sort(key=lambda x :(x%10,x//10))

cakes=deque(cakes)

cnt=0
while cakes:
    if cakes[0]==10:
        cakes.popleft()
        cnt+=1
    elif cakes[0]>10:
        if m==0:
            break
        cakes[0] -= 10
        cnt += 1
        m-=1
    else:
        cakes.popleft()

for cake in cakes:
    if cake==10:
        cnt+=1

print(cnt)

