
n=int(input())
box = list(map(int,input().split()))
ans=[-1]*n

stack=[0]
for i in range(1,n):
    while stack and box[stack[-1]]<box[i]:
        ans[stack.pop()] = box[i]
    stack.append(i)
print(*ans)