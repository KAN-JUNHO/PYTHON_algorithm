from collections import deque
box=deque([i for i in range(1,int(input())+1)])
while len(box)>1:
    box.popleft()
    box.append(box[0])
    box.popleft()
print(*box)