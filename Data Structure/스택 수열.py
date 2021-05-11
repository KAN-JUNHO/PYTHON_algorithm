n=int(input())
box=[int(input()) for i in range(n)]
stack=[i for i in range(1,n+1)]
ans=[]
answer=''
i=0
while stack or box:
    while ans and ans[-1] == box[0]:
        ans.pop()
        box.pop(0)
        answer+="-"
    if stack and box and box[0]!=stack[0]:
        answer+="+"
        ans.append(stack.pop(0))
    elif box and stack:
        answer+="+-"
        box.pop(0)
        stack.pop(0)
    else:
        if stack or box:
            print("NO")
            break
else:
    for i in answer:
        print(i)


