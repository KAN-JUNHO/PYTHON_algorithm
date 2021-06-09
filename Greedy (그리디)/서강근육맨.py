n=int(input())
box=list(map(int,input().split()))
box.sort()

hap=0
ans=0
while box:
    if len(box)%2==0:
        hap+=box.pop()
        hap+=box.pop(0)
    else:
        hap+=box.pop()

    ans=max(hap,ans)
    hap=0
print(ans)