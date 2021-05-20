N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))
val=0
for i in range(N):
    box=[0 for _ in range(d+1)]
    ans=0
    check=[]
    for j in range(k):
        box[sushi[(i+j)%N]]=1
        check.append(sushi[(i+j)%N])
    ans += box.count(1)

    if c not in check:
        ans+=1
    val=max(val,ans)
print(val)