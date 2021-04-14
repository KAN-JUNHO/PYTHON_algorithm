n=list(map(str,input().rstrip()))
flag=True
stack=[]
answer=[]

for i in n:
    if i=="<":
        if flag ==True and stack:
            stack.reverse()
            answer.append(stack[:])
            stack.clear()
        flag=False
        stack.append(i)
    elif i==">":
        flag=True
        stack.append(i)
        answer.append(stack[:])
        stack.clear()
    elif i==" ":
        if flag==True:
            stack.reverse()
            stack.append(i)
            answer.append(stack[:])
            stack.clear()
        else:
            stack.append(i)

    else:
        stack.append(i)
else:
    stack.reverse()
    answer.append(stack[:])
ans=[]
for i in answer:
    ans.extend(i)
print("".join(ans))