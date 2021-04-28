import itertools
n=int(input())
box=list(map(int,input().split()))
ans=0
a=list(itertools.permutations(box,n))
for num in a:
    hap = 0
    for i in range(0,n-1):
        hap+=abs(num[i]-num[i+1])
    ans=max(hap,ans)

print(ans)