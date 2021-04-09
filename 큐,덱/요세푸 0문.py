import collections

n, k = map(int, input().split())
result = []
queue = collections.deque([i for i in range(1, n + 1)])
while queue:
    for i in range(k):
        if i==k-1:
            result.append(queue.popleft())
        else:
            queue.append(queue[0])
            queue.popleft()

print("<" + ", ".join(list(map(str, result))) + ">")