import itertools
n,m=map(int,input().split())
box=list(map(int,input().split()))
box.sort()
for i in sorted(set(itertools.permutations(box,m))):
    print(*i)