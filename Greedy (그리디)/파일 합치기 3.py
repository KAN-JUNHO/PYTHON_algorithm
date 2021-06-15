import heapq
t=int(input())
for _ in range(t):
    k=int(input())
    ch=list(map(int,input().split()))

    heapq.heapify(ch)
    hap = 0


    while len(ch)>1:
        first =heapq.heappop(ch)
        second=heapq.heappop(ch)

        hap += first+second
        heapq.heappush(ch,first+second)
    print(hap)

