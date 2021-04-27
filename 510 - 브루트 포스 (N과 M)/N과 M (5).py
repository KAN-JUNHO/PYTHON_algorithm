import itertools
n,m=map(int,input().split())
box=list(map(int,input().split()))
a=list(itertools.permutations(box,m))
a.sort()

for i in a:
    print(*i)
