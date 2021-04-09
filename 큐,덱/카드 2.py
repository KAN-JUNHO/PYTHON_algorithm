from collections import deque
n = int(input())
box=deque()
for i in range(1,n+1):
    box.append(i)

while len(box)>1:
    box.popleft()
    a=box.popleft()
    box.append(a)

print(*box)