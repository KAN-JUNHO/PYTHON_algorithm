n=int(input())
road = list(map(int,input().split()))
gas = list(map(int,input().split()))

hap=0
m=gas[0]

for i in range(n-1):
    if gas[i]<m:
        m=gas[i]
    hap+= m*road[i]
print(hap)
