import itertools
import sys

n,s=map(int,input().split())
box=list(map(int,sys.stdin.readline().split()))

cnt=0
for i in range(1,n+1):
    for j in list(itertools.combinations(box,i)):
        if sum(j)==s:
            cnt+=1
print(cnt)