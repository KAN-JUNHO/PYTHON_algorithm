import heapq
import sys
heap=[]
n=int(input())
answer=[]
for _ in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    for i in a:
        heapq.heappush(heap,i)
        if len(heap)>n:
            heapq.heappop(heap)
print(heap[0])