n=int(input())
k=int(input())
road=list(map(int,input().split()))
dif=[]
road.sort()
if k>=n:
    print(0)
else:
    for i in range(n-1):
        dif.append(abs(road[i]-road[i+1]))

    dif.sort(reverse=True)
    for i in range(k-1):
        dif.pop(0)

    print(sum(dif))