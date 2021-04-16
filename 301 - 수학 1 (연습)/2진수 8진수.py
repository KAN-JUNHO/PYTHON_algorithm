n=list(map(str,input()))
box=[]
answer=0
n.reverse()
for i in range(0,len(n),3):
    a=n[i:i+3]
    a=list(map(int,a))
    for i in range(len(a)):
        answer+=a[i]*(2**i)
    box.append(str(answer))
    answer=0
print("".join(box[::-1]))

