n=int(input())
m=int(input())
if m!=0:
    no_button = list(map(str,input().split()))
    ans=abs(100-n)
    for num in range(1000001):
        num=str(num)
        for j in range(len(num)):
            if num[j] in no_button:
                break
            elif len(num)-1==j:
                ans=min(ans,abs(n-int(num))+len(num))
    print(ans)
else:
    print(len(str(m)))