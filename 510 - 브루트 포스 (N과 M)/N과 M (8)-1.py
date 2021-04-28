import itertools
n,m=map(int,input().split())
box=list(map(int,input().split()))
box.sort()

for i in itertools.combinations_with_replacement(box,m):
    print(*i)
