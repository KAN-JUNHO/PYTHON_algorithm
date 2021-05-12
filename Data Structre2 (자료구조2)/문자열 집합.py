import sys
n,m=map(int,sys.stdin.readline().split())

find={sys.stdin.readline().strip() for v in range(n)}

cnt=0
for i in range(m):
    a=sys.stdin.readline().strip()
    if a in find:
        cnt+=1
print(cnt)