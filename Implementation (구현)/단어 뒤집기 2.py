n=input()

stack=[]
box=[]
answer=[]
check=True
for i in n:
    if i=="<":
        if check and stack:
           stack.reverse()
           answer.append(stack[:])
           stack.clear()
        check=False
        stack.append(i)
    elif i==">":
        check = True
        stack.append(i)
        answer.append(stack[:])
        stack.clear()

    elif i==" ":
        if not check:
            stack.append(i)
        else:
            stack.reverse()
            stack.append(i)
            answer.append(stack[:])
            stack.clear()
    elif i.isalpha() or i.isdigit():
        stack.append(i)
else:
    stack.reverse()
    answer.append(stack[:])
ans=[]
for i in answer:
    ans.extend(i)
print("".join(ans))