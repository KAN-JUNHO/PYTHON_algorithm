import sys
n=int(input())
box=[list(map(int,sys.stdin.readline().split())) for i in range(n)]

box.sort(key=lambda x:x[0])

people=0
for i,j in box:
    people+=j

mid=people//2

if people%2==1:
    mid+=1

ans=0
for i,j in box:
    ans+=j
    if ans>=mid:
        print(i)
        break