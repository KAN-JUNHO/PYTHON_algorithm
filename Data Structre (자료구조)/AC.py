
import sys
from collections import deque
t=int(input())

for _ in range(t):
    p=sys.stdin.readline().strip()
    n=int(sys.stdin.readline())

    box=sys.stdin.readline()[1:-2].split(",")
    if box[0] =="":
        box=deque()
    else:
        box=deque(map(int,box))

    r=0
    check=False
    for i in p:
        if i=="R":
            r+=1
        elif i=="D":
            if box:
                if r%2==0:
                    box.popleft()
                else:
                    box.pop()
            else:
                check=True
                break
    if check:
        print("error")
    else:
        if r%2==1:
            box.reverse()
        box=list(box)
        print(str(box).replace(", ",","))