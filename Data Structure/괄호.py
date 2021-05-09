for i in range(int(input())):
    box = list(map(str,input().rstrip()))
    stack=[]
    for j in box:
        if j =="(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")