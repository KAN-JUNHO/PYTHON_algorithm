import itertools
while True:
    a=list(map(int,input().split()))
    if a[0]==0:
        break
    n=a[0]
    a=a[1:]
    com=list(itertools.combinations(a,6))
    for i in com:
        print(*i)
    print()