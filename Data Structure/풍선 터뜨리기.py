from collections import deque
n=int(input())
box=[[n,i+1] for i,n in enumerate(map(int,input().split()))]
box=deque(box)
answer=[]
while box:
    a=box.popleft()
    answer.append(a[1])
    if box and a[0]>0:
        for _ in range(a[0]-1):
            box.append(box.popleft())
    elif box and a[0]<0:
        for _ in range(-a[0]):
            box.appendleft(box.pop())
print(*answer)