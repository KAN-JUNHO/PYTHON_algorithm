from collections import deque
n=int(input())
skill=list(map(int,input().split()))
cards=deque(i for i in range(1,n+1))
ans=[]

while skill:
    s=skill.pop()
    c=cards.popleft()
    if s==1:
        ans.append(c)
    elif s==2:
        ans.insert(1,c)
    else:
        ans.append(c)
print(ans)
