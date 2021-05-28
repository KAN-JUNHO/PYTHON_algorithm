from collections import defaultdict
n,m=map(int,input().split())
DNA=[list(input()) for i in range(n)]
a=defaultdict(int)
box=[]
for i in range(m):
    for j in range(n):
        a[DNA[j][i]]+=1
    c = sorted(a.items(), key=lambda x:(-x[1],x[0]))
    box.append(c[0][0])
    a.clear()
cnt=0
for i in range(n):
    for j in range(m):
        if box[j]!=DNA[i][j]:
            cnt+=1

print("".join(box))
print(cnt)