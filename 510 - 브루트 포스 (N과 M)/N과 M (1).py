import itertools
n,m=map(int,input().split())
box = [i for i in range(1,n+1)]
a=list(itertools.permutations(box,m))
for i in a:
    print(*i)