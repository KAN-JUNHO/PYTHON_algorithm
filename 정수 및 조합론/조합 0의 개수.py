
n,k=map(int,input().split())

def fivecnt(v):
    cnt=0
    while v>=5:
        v//=5
        cnt+=v
    return cnt
def twocnt(v):
    cnt=0
    while v>=2:
        v//=2
        cnt+=v
    return cnt

print(min(twocnt(n)-twocnt(k)-twocnt(n-k),fivecnt(n)-fivecnt(k)-fivecnt(n-k)))