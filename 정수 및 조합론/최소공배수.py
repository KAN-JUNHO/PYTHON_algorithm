n=int(input())

for i in range(n):
    a,b=list(map(int,input().split()))
    c,d = a,b
    while b !=0:
        a = a%b
        a,b = b,a
    print(c*d//a)
