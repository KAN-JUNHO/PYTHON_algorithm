import sys

n=int(input())
box = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
check=[False]*n
answer=10e9
def dfs(cur,cost):
    global answer
    if cur==0 and all(check):
        answer = min(answer, cost)
    else:
        for next in range(n):
            if box[cur][next] and not check[next]:
                check[next]=True
                dfs(next,cost+box[cur][next])
                check[next]=False
dfs(0,0)

print(answer)