import sys
input = sys.stdin.readline

n,m=map(int,input().split())
boxes=list(map(int,input().split()))

hap=0
cnt=0
if n!=0:
    while boxes:
        while boxes and boxes[-1]+hap<=m:
            hap+=boxes[-1]
            boxes.pop()
        hap=0
        cnt+=1
    print(cnt)
else:
    print(0)
