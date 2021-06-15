import heapq
n=int(input())

card=[int(input()) for _ in range(n)]
heapq.heapify(card)

hap=0
while len(card)>1:

    first=heapq.heappop(card)
    second=heapq.heappop(card)
    hap += first+second
    heapq.heappush(card,first+second)

print(hap)