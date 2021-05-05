n=int(input())
box = list(map(int,input().split()))
flag=[False]*(sum(box)+2)
def solve(idx,hap):
    if n==idx:
        flag[hap]=True
        return
    solve(idx+1,hap+box[idx])
    solve(idx+1,hap)
solve(0,0)
for i in range(len(flag)):
    if flag[i]==False:
        print(i)
        break