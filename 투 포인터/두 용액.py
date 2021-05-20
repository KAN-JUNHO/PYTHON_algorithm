n=int(input())
box=list(map(int,input().split()))
box.sort()
val=10e9
answer=[]
left=0
right=n-1
while left<right:
    hap=box[left]+box[right]
    if abs(hap)<val:
        answer=[box[left],box[right]]
        val=abs(hap)
    if hap>=0:
        right-=1
    else:
        left+=1

print(*answer)