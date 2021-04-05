n,m =map(int,input().split())
coin=[int(input()) for _ in range(n)]
coin.sort(reverse=True)
cnt=0
hap=0
while m!=0:
    for i in range(len(coin)):
        if m>=coin[i]:
            cnt=m//coin[i]
            m -= cnt*coin[i]
            hap+=cnt
            break
        else:
            del coin[0]
            break
print(hap)
