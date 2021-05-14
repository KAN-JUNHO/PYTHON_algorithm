from collections import deque
n=int(input())
tree=[[] for i in range(n+1)]
for i in range(n-1):
    v,w=map(int,input().split())
    tree[w].append(v)
    tree[v].append(w)
check=[False]*(n+1)
que= deque()
que.append(1)
answer=[]
while que:
    node = que.popleft()
    for i in tree[node]:
        if not check[i]:
            answer.append([i,node])
            que.append(i)
            check[i]=True
answer.sort()
for i in answer[1:]:
    print(i[1])