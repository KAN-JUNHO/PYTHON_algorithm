import itertools
n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]

home=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            home.append((i,j))
        elif board[i][j]==2:
            chicken.append((i,j))
box=[]
ans=[]
answer=10e9
for ch in itertools.combinations(chicken,m):
    for h in home:
        for c in ch:
            box.append(abs(c[0]-h[0])+abs(c[1]-h[1]))
        ans.append(min(box))
        box.clear()
    answer=min(answer,sum(ans))
    ans.clear()
print(answer)