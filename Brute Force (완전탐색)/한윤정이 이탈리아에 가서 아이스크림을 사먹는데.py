N, M = map(int, input().split())
cnt = 0
if N < 3:
    print(cnt)
else:
    graph={i:[] for i in range(1,N+1)}
    for _ in range(M):
        v,w=map(int,input().split())
        graph[v].append(w)
        graph[w].append(v)
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if j not in graph[i]:
                for k in  range(j+1,N+1):
                    if k not in graph[i] and k not in graph[j]:
                        cnt+=1
    print(cnt)