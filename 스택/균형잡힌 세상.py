import sys

while True:
    arr=sys.stdin.readline().rstrip()
    print(arr)
    box = []
    if arr==".":
        break
    check=True
    for i in arr:
        if i in "([":
            box.append(i)
        elif i==")":
            if len(box)>0 and "(" == box[-1]:
                box.pop()
            else:
                check=False
                break
        elif i=="]":
            if  len(box)>0 and "[" == box[-1]:
                box.pop()
            else:
                check=False
                break

    if check== True and not box:
        print("yes")
    else:
        print("no")

