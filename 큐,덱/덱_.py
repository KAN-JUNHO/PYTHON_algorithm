import collections
import sys
from  collections import deque
n= int(input())
que=collections.deque()
cnt=0

for i in range(n):
    box = sys.stdin.readline().split()
    if box[0] == "push_front":
        que.appendleft(box[1])
        cnt+=1
    elif box[0] == "push_back":
        que.append(box[1])
        cnt+=1
    elif box[0] == "pop_front":
        if cnt==0:
            print(-1)
        else:
            print(que.popleft())
            cnt-=1
    elif box[0] == "pop_back":
        if cnt == 0:
            print(-1)
        else:
            print(que.pop())
            cnt -= 1
    elif box[0] == "size":
        print(cnt)
    elif box[0] == "empty":
        if cnt==0:
            print(1)
        else:
            print(0)
    elif box[0] == "front":
        if cnt==0:
            print(-1)
        else:
            print(que[0])
    elif box[0] == "back":
        if cnt==0:
            print(-1)
        else:
            print(que[-1])