import itertools
n,k=map(int,input().split())
num=list(map(int,input().split()))
ans = []
v=len(str(n))
for i in range(1,v+1):
    a=list(itertools.product(num,repeat=i))
    for j in a:
        temp="".join(map(str,j))
        if n>=int(temp):
            ans.append(int(temp))

print(max(ans))
