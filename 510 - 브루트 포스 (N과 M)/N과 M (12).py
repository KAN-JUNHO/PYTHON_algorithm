import itertools
n,m=map(int,input().split())
box=list(map(int,input().split()))
box.sort()
a=list(itertools.combinations_with_replacement(box,m))
a=sorted(set(a))

for i in a:
    print(*i)