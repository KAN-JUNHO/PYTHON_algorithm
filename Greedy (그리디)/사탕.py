t=int(input())

for _ in range(t):
    candy, box = map(int, input().split())
    size = []
    for i in range(box):
        w,h=map(int,input().split())
        size.append(w*h)
    size.sort()

    ans=0
    while candy>0:
        candy-=size.pop()
        ans+=1
    print(ans)