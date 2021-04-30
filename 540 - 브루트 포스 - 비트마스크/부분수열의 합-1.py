import sys
n,s=map(int,input().split())
box=list(map(int,sys.stdin.readline().split()))
ans=[]
cnt=0

def dfs(pos,length):
    global cnt
    if pos==length:
        if sum(ans)==s:
            cnt+=1
        return
    for i in range(pos,len(box)):
        ans.append(box[i])
        dfs(i+1,length)
        ans.pop()
for i in range(1,n+1):
    dfs(0,i)

print(cnt)