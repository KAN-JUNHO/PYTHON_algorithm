n,s = map(int,input().split())
box=list(map(int,input().split()))
cnt=0
def dfs(idx,hap):
    global cnt
    if idx>=n:
        if s==hap:
            cnt+=1
            return
    else:
        dfs(idx+1,hap+box[idx])
        dfs(idx+1,hap)

dfs(0,0)
if s!=0:
    print(cnt)
else:
    print(cnt-1)