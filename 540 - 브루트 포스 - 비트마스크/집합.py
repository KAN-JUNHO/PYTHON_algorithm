import sys
n=int(sys.stdin.readline())
s=set()
for _ in range(n):
    order = sys.stdin.readline().strip().split()
    print(order)
    if order[0]=="all":
        s.clear()
        s=set([i for i in range(1,21)])
        continue
    elif order[0]=="empty":
        s.clear()
        continue

    num=int(order[1])
    if order[0] == "add":
        s.add(num)
    elif order[0] =="remove":
        s.discard(num)
    elif order[0]=="check":
        if num in s:
            print(1)
        else:
            print(0)
    elif order[0]=="toggle":
        if num in s:
            s.discard(num)
        else:
            s.add(num)
