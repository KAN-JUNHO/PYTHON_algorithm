from collections import deque
n=int(input())

for _ in range(n):
    box=deque(input())
    left,right=[],[]

    while box:
        if box[0]=="<":
            if left:
                right.append(left.pop())
        elif box[0]==">":
            if right:
                left.append(right.pop())
        elif box[0]=="-":
            if left:
                left.pop()
        else:
            left.append(box[0])
        box.popleft()
    print("".join(left)+"".join(reversed(right)))