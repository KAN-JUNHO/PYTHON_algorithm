h,w=map(int,input().split())
box=list(map(int,input().split()))
ans=0
for i in range(len(box)):
    max_left=max(box[:i+1])
    max_right=max(box[i:])
    choice=min(max_left,max_right)
    ans+=abs(choice-box[i])
print(ans)