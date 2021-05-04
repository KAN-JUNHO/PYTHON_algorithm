import collections
def dfs(idx):
    if len(box)==6:
        print(*box)
        return

    for i in range(idx,k):
        if not check[i]:
            check[i]=True
            box.append(lotto[i])
            dfs(i+1)
            box.pop()
            check[i]=False

while True:
    lotto = collections.deque(map(int,input().split()))
    if not lotto[0]:
        break
    k=lotto.popleft()
    check=[False]*k
    box=[]
    dfs(0)
    print()