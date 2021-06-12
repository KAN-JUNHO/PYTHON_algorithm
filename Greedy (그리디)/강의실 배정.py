import heapq
import sys

N = int(input())

box = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
box.sort()
ans=[]

for i in range(N):
    if ans and ans[0] <= box[i][0]:
        heapq.heappop(ans)
    heapq.heappush(ans,box[i][1])

print(ans)