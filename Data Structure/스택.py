import sys
stack=[]
for i in range(int(sys.stdin.readline())):
    order=sys.stdin.readline().split()
    if order[0]=="push":
            stack.append(order[1])
    order=order[0]
    if order=="pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if order=="size":
        print(len(stack))
    if order=="empty":
        if stack:
            print(0)
        else:
            print(1)

    if order == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)