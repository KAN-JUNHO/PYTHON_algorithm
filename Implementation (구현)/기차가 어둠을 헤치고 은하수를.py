import  sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
train=[deque([0]*20) for _ in range(n)]
for _ in range(m):
    box=list(map(int,sys.stdin.readline().split()))
    if box[0]==1:
        train[box[1]-1][box[2]-1]=1
    elif box[0]==2:
        train[box[1]-1][box[2]-1]=0
    elif box[0]==3:
        train[box[1]-1].rotate(1)
        train[box[1]-1][0]=0
    else:
        train[box[1]-1].rotate(-1)
        train[box[1]-1][19]=0
answer=[]
for i in train:
    if i not in answer:
        answer.append(i)
print(len(answer))

