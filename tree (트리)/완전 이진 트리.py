import sys
n=int(input())
box=list(map(int,sys.stdin.readline().split()))

i=0
answer=[]
ans=[]
while box:
    if i>len(box)-1:
        i=0
        ans.append(answer[:])
        answer.clear()
    answer.extend([box.pop(i)])
    i+=1
ans.append(answer)

ans.reverse()
for i in ans:
    print(*i)