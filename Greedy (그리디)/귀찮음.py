from collections import deque
n=int(input())
box=list(map(int,input().split()))
box.sort()
box=deque(box)
hap=0
temp=[]

while len(box)!=1:
    while len(box)>1:
        a=box.popleft()
        b=box.pop()
        hap+=a*b
        temp.append(a+b)
    box.extend(temp)
    temp=[]
print(hap)
