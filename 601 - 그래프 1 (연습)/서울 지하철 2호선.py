import collections
import sys
sys.setrecursionlimit(100000)
t=int(input())
station = [[] for i in range(t)]
cycle=False
iscycle = [False]*t
check = [-1]*t

def dfs(cur,start, cnt):
    global cycle
    if cur==start and cnt>=2:
        cycle=True
        return
    visit[cur] = True
    for n in station[cur]:
        if not visit[n]:
            dfs(n,start,cnt+1)
        elif n==start and cnt>=2:
            dfs(n,start,cnt)
for i in range(t):
    a,b = map(int,input().split())
    station[a-1].append(b-1)
    station[b-1].append(a-1)

for i in range(t):
    visit = [False] * t
    cycle=False
    dfs(i,i,0)
    if cycle:
        iscycle[i]=True
q= collections.deque()
for i in range(t):
    if iscycle[i]:
        check[i]=0
        q.append(i)
while q:
    cur =  q.popleft()
    for i in station[cur]:
        if check[i]==-1:
            q.append(i)
            check[i] = check[cur]+1
print(*check)