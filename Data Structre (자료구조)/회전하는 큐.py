from collections import deque

m,n = map(int,input().split())
box=[i for i in range(1,m+1)]
box=deque(box)
ans=deque(map(int,input().split()))

cnt=0
while ans:
    if box[0]== ans[0]:
        box.popleft()
        ans.popleft()
    else:
        idx=box.index(ans[0])
        if len(box)//2 <idx:
            box.rotate(1)
            cnt+=1
        else:
            box.rotate(-1)
            cnt+=1
print(cnt)