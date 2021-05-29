import itertools
n=int(input())
k=int(input())
cards=list(int(input()) for i in range(n))
permu = list(itertools.permutations(cards,k))
ans=[]
for i in permu:
    a="".join(map(str,i))
    if a not in ans:
        ans.append(a)
print(len(ans))