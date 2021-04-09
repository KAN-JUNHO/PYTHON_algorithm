import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
stack=deque()
for i in range(n):
    box=list(map(str,sys.stdin.readline().rstrip().split()))
    if box[0]=="push":
        stack.append(box[1])
    elif box[0] == "pop":
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif box[0] == "size":
        print(len(stack))
    elif box[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif box[0] =="front":
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif box[0] =="back":
        if stack:
            print(stack[-1])
        else:
            print(-1)