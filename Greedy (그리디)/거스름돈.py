n=int(input())
cnt=0
while n>0:
    if n%5==0:
        print(n//5+cnt)
        break
    n-=2
    cnt+=1
if n<0:
    print(-1)
