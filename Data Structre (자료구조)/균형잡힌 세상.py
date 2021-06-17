

while True:
    n=input()
    if n==".":
        break
    stack=[]
    for i in n:
        if i=="(" or i== "[":
            stack.append(i)
        elif i=="]" or i==")":
            if stack and stack[-1]=="("and i==")":
                stack.pop()
            elif stack and stack[-1]=="[" and i=="]":
                stack.pop()
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")