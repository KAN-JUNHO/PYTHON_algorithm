import sys
n,m=map(int,sys.stdin.readline().split())
box=list(map(int,sys.stdin.readline().split()))
for i in range(1,len(box)):
    box[i]+=box[i-1]
box.insert(0,0)
for i in range(m):
    start,end=map(int,sys.stdin.readline().split())
    print(box[end]-box[start-1])