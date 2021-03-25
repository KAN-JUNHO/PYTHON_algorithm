import sys
n =int(input())
for _ in range(n):
    box=[]
    a,b = list(map(str,sys.stdin.readline().split()))
    for i in range(len(b)):
        box.append(int(a)*b[i])
    box1 = "".join(box)
    print(box1)

