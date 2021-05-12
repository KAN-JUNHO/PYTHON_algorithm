n=int(input())
box=list(map(int,input().split()))
stack=[]
answer=[]
for i in range(len(box)):
    while stack:
        if box[i]<stack[-1][1]:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i,box[i]])
print(*answer)