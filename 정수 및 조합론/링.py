def gcd(a,b):
    while b!=0:
        n=a%b
        a,b=b,n
    return a
n = int(input())
ring = list(map(int,input().split()))

for  i in range(1,n):
    g=gcd(ring[0], ring[i])
    print("{0}/{1}".format(ring[0]//g,ring[i]//g))