import sys
input=sys.stdin.readline
n=int(input())

member=dict()
for i in range(n):
    a=input()
    if a not in member:
        member[a]=1
    else:
        member[a]+=1

for i in range(n-1):
    a=input()
    if a in member:
        member[a]-=1

for i in member:
    if member[i]:
        print(i)
        break