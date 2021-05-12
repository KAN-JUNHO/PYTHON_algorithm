import sys
box = sys.stdin.readline().rstrip()
stack = []

for i in box:
    if i == ")":
        temp=0
        while stack:
            top = stack.pop()
            if top=="(":
                if temp==0:
                    stack.append(2)
                else:
                    stack.append(2*temp)
                break

            elif top=="[":
                print(0)
                exit(0)
            else:
                temp+=int(top)
    elif i == "]":
        temp = 0
        while stack:
            top = stack.pop()
            if top == "[":
                if temp==0:
                    stack.append(3)
                else:
                    stack.append(3*temp)
                break
            elif top == "(":
                print(0)
                exit(0)
            else:
                temp += int(top)
    else:
        stack.append(i)
hap=0
for i in stack:
    if i=="(" or i=="[":
        print(0)
        exit(0)
    else:
        hap+=i
print(hap)