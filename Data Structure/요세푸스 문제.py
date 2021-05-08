n,k=map(int,input().split())
box=[i for i in range(1,n+1)]
ans=[]
i=0
while box:
    i+=k-1
    while i>len(box)-1:
       i=i-len(box)
    ans.append(str(box.pop(i)))
print("<",", ".join(ans),">",sep='')