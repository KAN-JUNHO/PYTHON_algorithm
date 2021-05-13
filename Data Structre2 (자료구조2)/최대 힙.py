import heapq
import sys
n=int(sys.stdin.readline())
box=[]
for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if box:
            print(heapq.heappop(box)[1])
        else:
            print(0)
    else:
        heapq.heappush(box,[-x,x])