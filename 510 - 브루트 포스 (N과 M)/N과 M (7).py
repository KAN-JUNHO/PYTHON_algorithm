import itertools
n,m=map(int,input().split())
box=list(map(int,input().split()))
box.sort()
for i in list(itertools.product(box,repeat=m)):
    print(*i)