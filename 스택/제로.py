import sys
from collections import deque

n=int(sys.stdin.readline())
box=deque()
for i in range(n):
    a=int(sys.stdin.readline())
    if a!=0:
        box.append(a)
    else:
        box.pop()
print(sum(box))