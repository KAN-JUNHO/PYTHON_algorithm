n=int(input())
v=2
while n!=1:
    if n%v==0:
       n=n//v
       print(v)
    else:
        v+=1