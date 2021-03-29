n = int(input())

for i in range(1,n+1):
    cnt=i
    test = i
    while True:
        cnt += test%10
        test = test//10
        if test==0:
            break
    if cnt == n:
        print(i)
        break
else:
    print(0)
