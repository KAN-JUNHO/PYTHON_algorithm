n=int(input())
crane=list(map(int,input().split()))
m=int(input())
box=list(map(int,input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
check=[False]*m

cnt=0
if box[0]>crane[0]:
    print(-1)
else:
    while box:
        cnt+=1
        for i in crane:
            for j in range(len(box)):
                if box[j]<=i:
                    del box[j]
                    break
    print(cnt)