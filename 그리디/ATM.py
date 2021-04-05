n=int(input())
atm = list(map(int,input().split()))
atm.sort()

hap=0
for i in range(1,n+1):
    for j in range(i):
        hap+=atm[j]

print(hap)