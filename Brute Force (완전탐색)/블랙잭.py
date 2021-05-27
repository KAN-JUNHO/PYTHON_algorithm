n,m=map(int,input().split())
cards=list(map(int,input().split()))
box=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            hap=0
            hap=cards[i]+cards[j]+cards[k]
            if hap<=m:
                box.append(hap)

print(max(box))