box=input().rstrip()
stack=[]
cnt=0
for i in range(len(box)):
    if box[i]=="(":
        stack.append("(")
    elif box[i-1]=="(":
        stack.pop()
        cnt+=len(stack)
    else:
        stack.pop()
        cnt+=1
print(cnt)