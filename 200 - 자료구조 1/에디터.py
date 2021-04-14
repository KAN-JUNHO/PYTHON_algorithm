import sys

stack_a=list(map(str,sys.stdin.readline().rstrip()))
stack_b=[]
n=int(sys.stdin.readline())
pos=len(stack_a)
for i in range(n):
    box=sys.stdin.readline().split()
    if box[0]=="L" and stack_a:
        stack_b.append(stack_a.pop())
    elif box[0]=="D" and stack_b:
        stack_a.append(stack_b.pop())
    elif box[0]=="B" and stack_a:
        stack_a.pop()
    elif box[0]=="P":
        stack_a.append(box[1])
print("".join(stack_a+stack_b[::-1]))
