import sys
from collections import deque

deque=deque()
for i in range(int(input())):
    order = sys.stdin.readline().rstrip().split()
    if len(order)>1:
        if order[0]=="push_front":
           deque.appendleft(order[1])
        elif order[0]=="push_back":
            deque.append(order[1])

    else:
        order=order[0]
        if order=="pop_front":
            if deque:
                print(deque.popleft())
            else:
                print(-1)
        elif order == "pop_back":
            if deque:
                print(deque.pop())
            else:
                print(-1)
        elif order=="size":
            print(len(deque))

        elif order =="empty":
            if deque:
                print(0)
            else:
                print(1)

        elif order=="front":
            if deque:
                print(deque[0])
            else:
                print(-1)

        elif order == "back":
            if deque:
                print(deque[-1])
            else:
                print(-1)