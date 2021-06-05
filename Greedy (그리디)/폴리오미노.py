n=list(map(str,input()))
n.append(".")
cnt=0
box=[]
check=False

for i in n:
    if i=="X":
        cnt+=1
    else:
        while cnt>=4:
            box.append("AAAA")
            cnt-=4
        if cnt==2:
            box.append("BB")
            cnt-=2
        elif cnt!=0:
            check=True
        box.append(".")
box.pop()
if check:
    print(-1)
else:
    print("".join(box))
