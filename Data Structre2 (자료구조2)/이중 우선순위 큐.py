import heapq
import sys
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    min_heap=[]
    max_heap=[]
    visit = [False] * (n + 1)
    for j in range(n):

        order,n = map(str,input().split())
        n=int(n)
        if order=="I":
            heapq.heappush(min_heap,[n,j])
            heapq.heappush(max_heap,[-n,j])
            visit[j]=True
        elif order=="D":
            if n==1:
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]]=False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]]=False
                    heapq.heappop(min_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print("EMPTY")