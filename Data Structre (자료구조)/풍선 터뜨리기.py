from collections import deque
n=int(input())
q = deque(enumerate(map(int,input().split())))
answer=[]
print(q)
while True:
    idx,move = q.popleft()
    answer.append(idx+1)

    if not q:
        break
    if move>0:
        q.rotate(-(move-1))
    elif move<0:
        q.rotate(-move)
print(answer)