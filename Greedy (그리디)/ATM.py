n=int(input())
atm=list(map(int,input().split()))

atm.sort()
hap=0
for i in range(n):
    hap+=sum(atm[:i+1])
print(hap)