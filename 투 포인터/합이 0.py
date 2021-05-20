n=int(input())
box=list(map(int,input().split()))
box.sort()
print(box)
ans=0
for i in range(n-2):
    left=i+1
    right=n-1
    target=-box[i]
    mx_idx=n
    while left<right:
        tmp = box[left] + box[right]
        if tmp<target:
            left+=1
        elif tmp>target:
            right-=1
        else:
            if box[left]==box[right]:
                ans+=right-left
            else:
                if mx_idx>right:
                    mx_idx = right
                    while mx_idx>=0 and box[mx_idx-1]==box[right]:
                        mx_idx-=1
                ans+=right-mx_idx+1
            left+=1
print(ans)