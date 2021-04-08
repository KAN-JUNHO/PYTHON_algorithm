import sys

n=int(sys.stdin.readline())

for i in range(n):
    arr=sys.stdin.readline().replace("\n","")
    box=[]
    for j in arr:
        if j=="(":
            box.append(j)
        else:
            if not box:
                print("NO")
                break
            else:
                box.pop()
    else:
        if box:
            print("NO")
        else:
            print("YES")