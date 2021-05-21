n=int(input())
cows={}
cnt=0
for _ in range(n):
    a,b=map(int,input().split())
    if a not in cows:
        cows[a]=b
    else:
        if cows[a]!=b:
            cnt+=1
            cows[a]=b
print(cnt)