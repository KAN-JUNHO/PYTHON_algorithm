def dfs(pos):
    if len(box)==6:
        print(*box)
        return
    for i in range(pos,len(a)):
        if check[i]==False:
            box.append(a[i])
            check[i]=True
            dfs(i)
            check[i]=False
            box.pop()
while True:
    box=[]
    a=list(map(int,input().split()))
    if a[0]==0:
        break

    a = a[1:]
    check=[False]*len(a)
    dfs(0)
    print()