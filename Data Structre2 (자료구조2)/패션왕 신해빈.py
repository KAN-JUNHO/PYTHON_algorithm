t=int(input())

for _ in range(t):
    cloth=dict()
    n=int(input())
    for i in range(n):
        a,b=map(str,input().split())
        if b in cloth:
            cloth[b]+=1
        else:
            cloth[b]=1
    v=1
    for i in cloth.values():
       v*=(i+1)
    print(v-1)