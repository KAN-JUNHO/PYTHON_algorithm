n,k=map(int,input().split())

hap=k*(k+1)//2
if hap>n:
    print(-1)
elif (n-hap)%k==0:
    print(k-1)
else:
    print(k)