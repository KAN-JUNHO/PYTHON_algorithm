n=input()

cnt=0
def dfs(num):
    global cnt
    if len(n) == 1:
        cnt+=1
        return

    l = set(num)
    if len(l)==1:
        cnt+=1
        return
    else:
        dfs(num[1:])
        dfs(num[:-1])
dfs(n)
print(cnt)