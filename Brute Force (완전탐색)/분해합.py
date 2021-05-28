n=int(input())
for i in range(n):
    val=i
    temp=0
    while i>0:
        a=i%10
        i=i//10
        temp+=a
    ans=temp+val
    if ans==n:
        print(val)
        break
else:
    print(0)