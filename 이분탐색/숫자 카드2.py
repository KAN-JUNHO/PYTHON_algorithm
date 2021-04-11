from collections import Counter

m=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))

a=Counter(a)

answer=[]

for i in b:
    if i in a.keys():
        answer.append(a[i])
    else:
        answer.append(0)

print(*answer)