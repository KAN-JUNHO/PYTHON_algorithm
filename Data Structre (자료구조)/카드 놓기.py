from collections import deque
n=int(input())
skill=deque(map(int,input().split()))
cards=deque(i for i in range(1,n+1))
ans=deque()

while skill:
    s=skill.pop()
    c=cards.popleft()

    if s==1:
        ans.appendleft(c)
    elif s==2:
        ans.insert(1,c)
print(ans)
# 5             1 5 2 3 4
# 2 3 3 2 1
# 1 2 3 4 5

2