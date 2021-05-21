n=int(input())
box=list(map(int,input().split()))
box.sort()
left=0
right=n-1
val=10e9
ans=[10e9,10e9]
while left<right:
    hap=box[left]+box[right]
    if abs(val)>abs(hap):
        ans[0]=box[left]
        ans[1]=box[right]
        val=hap
        if val==0:
            break
    if hap<0:
        left+=1
    else:
        right-=1
print(*ans)