t = int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    box=[[1]*n for _ in range(k+1)]
    print(box)
    for j in range(k):
        for k in range(1,n+1):
            print()