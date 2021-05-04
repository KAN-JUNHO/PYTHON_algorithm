n=int(input())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

