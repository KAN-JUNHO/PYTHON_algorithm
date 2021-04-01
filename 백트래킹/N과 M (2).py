import itertools
n,m = map(int,input().split())
a=list(itertools.combinations(range(1,n+1),m))
for i in a:
    print(*i)