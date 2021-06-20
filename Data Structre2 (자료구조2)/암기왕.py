import sys
t=int(sys.stdin.readline())

for _ in range(t):
    num1=int(sys.stdin.readline())
    note1=set(map(int,sys.stdin.readline().split()))

    num2=int(sys.stdin.readline())
    note2=list(map(int,sys.stdin.readline().split()))

    ans=[]
    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)