n,m=map(int,input().split())
box=list(map(int,input().split()))
ans=[]
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
for i in box:
    ans.append(abs(m-i))

answer=min(ans)
for i in range(len(ans)):
    answer=gcd(answer,ans[i])

print(answer)