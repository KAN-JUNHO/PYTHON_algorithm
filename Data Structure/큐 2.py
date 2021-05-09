import sys
from collections import deque

stack=deque()
for i in range(int(input())):
    order = sys.stdin.readline().split()
    if len(order)>1:
       stack.append(order[1])
    else:
        order=order[0]
        if order=="pop":
            if stack:
                print(stack.popleft())
            else:
                print(-1)
        if order=="size":
            print(len(stack))
        if order=="empty":
            if stack:
                print(0)
            else:
                print(1)
        if order=="front":
            if stack:
                print(stack[0])
            else:
                print(-1)
        if order=="back":
            if stack:
                print(stack[-1])
            else:
                print(-1)