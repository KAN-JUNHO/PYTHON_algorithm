t=int(input())

for _ in range(t):
    n=int(input())
    a=input()
    b=input()
    box={}
    for i in range(n):
        if a[i]!=b[i]:
            if not a[i] in box:
                box[a[i]]=1
            else:
                box[a[i]]+=1
    ans=max(box.values())
    print(ans)