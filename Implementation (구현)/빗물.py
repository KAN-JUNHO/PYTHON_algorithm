h,w=map(int,input().split())
block=list(map(int,input().split()))
hap=0
for i in range(1,w-1):
    left=max(block[:i])
    right=max(block[i+1:])
    val=min(left,right)
    if val>=block[i]:
        hap+=val-block[i]
print(hap)