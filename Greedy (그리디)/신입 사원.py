import sys

input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    result=[]
    for i in range(n):
        result.append(list(map(int,input().split())))

    result.sort(key=lambda x:x[0])

    min_v=result[0][1]
    cnt=1
    for i in range(1,n):
        if result[i][1]<min_v:
            min_v = result[i][1]
            cnt+=1
    print(cnt)