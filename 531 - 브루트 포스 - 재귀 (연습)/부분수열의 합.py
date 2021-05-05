n,s=map(int,input().split())
box=list(map(int,input().split()))
ans=[]
cnt=0
def solve(idx,hap):
    global cnt
    if n==idx:
        return
    hap+=box[idx]
    if hap==s:
        cnt+=1
    solve(idx+1,hap)
    solve(idx+1,hap-box[idx])

solve(0,0)
print(cnt)