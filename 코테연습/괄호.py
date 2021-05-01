inputString=">_<"
answer = []
stack = []
cnt=0
for pos,i in enumerate(inputString):
    if i == "[" or i == "(" or i == "{" or i=="<":
        stack.append([pos,i])
    if stack:
        if (i == "]" and stack[-1][1]=="[") or (i == ")" and stack[-1][1]=="(") or( i == "}" and stack[-1][1]=="{") or (i==">" and stack[-1][1]=="<"):
            stack.pop()
            cnt+=1
        elif i=="]" or i==")" or i=="}" or i==">":
            answer.append([pos,i])
    else:
        if i=="]" or i==")" or i=="}" or i==">":
            print(0)
if len(stack)==0:
    print(cnt)
else:
    if answer:
        print(-answer[0][0])
    else:
        print(-len(inputString)+1)
