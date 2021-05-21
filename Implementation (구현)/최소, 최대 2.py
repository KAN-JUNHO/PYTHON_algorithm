t=int(input())
for i in range(t):
    n=int(input())
    box=list(map(int,input().split()))
    print(min(box),max(box))