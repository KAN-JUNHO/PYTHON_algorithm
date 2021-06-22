import heapq
import sys

input=sys.stdin.readline
n=int(input())

box=[]
for _ in range(n):
    a=int(input())
    if a==0:
        if box:
            print(box[0])
            heapq.heappop(box)
        else:
            print(0)
    else:
        heapq.heappush(box,a)
