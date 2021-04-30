n,m=map(int,input().split())
box=[]
for i in range(m):
    box.append(list(map(int,input().split())))


def dfs(pos):
    if all(check):
        print(1)
        return
    if box[pos][1]<n and pos<m:
        check[pos]=True
        check[box[pos][1]]=True
        if box[pos][1]<len(box):
            dfs(box[pos][1])
    else:
        print(0)
for i in range(n):
    check = [False] * n
    dfs(i)