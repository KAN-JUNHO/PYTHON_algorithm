n=int(input())
snow = list(map(int,input().split()))
snow.sort()
ans=10e9
for i in range(n):
    for j in range(i+3,n):
        left=i+1
        right=j-1

        while right>left:
            hap = snow[i]+snow[j]-snow[left]-snow[right]
            ans=min(abs(ans),abs(hap))
            if hap<0:
                right-=1
            else:
                left+=1
print(ans)