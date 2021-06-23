s=list(map(int,input()))
one=0
zero=0
for i in range(1,len(s)):
    if s[i-1]!=s[i]:
        if s[i]==1:
            one+=1
        else:
            zero+=1


a=(min(one,zero))

if (one+zero)%2==0:
    print(a)
else:
    print(a+1)