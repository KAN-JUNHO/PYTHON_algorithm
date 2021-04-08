import sys

def push(num):
    stack.append(num)
def pop():
    if not stack:
        print(-1)
    else:
        print(stack[-1])
        del stack[-1]
def size():
    print(len(stack))
def empty():
    if not stack:
        print(1)
    else:
        print(0)
def top():
    if not stack:
        print(-1)
    else:
        print(stack[-1])

n=int(sys.stdin.readline())
stack = []
for i in range(n):
    c= sys.stdin.readline().split()
    if c[0]=="push":
        push(c[1])
    elif c[0]=="pop":
        pop()
    elif c[0]=="size":
        size()
    elif c[0]=="empty":
        empty()
    else:
        top()
