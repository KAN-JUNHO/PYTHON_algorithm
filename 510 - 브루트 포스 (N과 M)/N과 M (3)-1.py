import itertools
n,m=map(int,input().split())
box=[]
for i in range(1,n+1):
    box.append(i)


for i in list(itertools.product(box,repeat=m)):
    print(*i)