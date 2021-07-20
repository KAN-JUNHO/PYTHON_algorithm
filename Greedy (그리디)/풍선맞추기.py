n=int(input())
balloon=list(map(int,input().split()))
check=[0]*1000000
cnt=0

for i in balloon:
    if check[i]==0:
        cnt+=1
        check[i-1]+=1
    else:
        check[i]-=1
        check[i-1]+=1

print(cnt)
