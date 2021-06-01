import itertools
n=int(input())
box = [list(map(int,input().split())) for i in range(n)]
ans=10e9
com=[]
for i in range(1,n+1):
    com.append(list(itertools.combinations(box,i)))

for i in com:
    for j in i:
        sour, bitter = 1, 0
        for k in j:
            sour*=k[0]
            bitter+=k[1]
        ans=min(ans,abs(bitter-sour))
print(ans)