n,k=map(int,input().split())
coins=[int(input()) for i in range(n)]
cnt=0
while k!=0:
    if k>=coins[-1]:
        cnt+=k//coins[-1]
        k=k%coins[-1]
    else:
        coins.pop()

print(cnt)