m = int(input())
i=2
while 1!=m:
    if m%i==0:
        m=m/i
        print(i)
    else:
        i+=1