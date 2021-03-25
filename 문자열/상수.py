a,b = list(map(str,input().split()))
a_=""
b_=""
for i in range(len(a)-1,-1,-1):
    a_+=a[i]
for i in range(len(b)-1,-1,-1):
    b_+=b[i]

if a_>b_:
    print(a_)
else:
    print(b_)