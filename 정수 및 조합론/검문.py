import math
n=int(input())
box=[]
for i in range(n):
    box.append(int(input()))

a=max(box)
a=int(math.sqrt(a))
ans=[]
for i in range(2,a):
    namu=box[0]%i
    for j in range(1,len(box)):
        if box[j]%i!=namu:
            break
    else:
        ans.append(i)
print(ans)