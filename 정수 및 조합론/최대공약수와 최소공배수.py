n,m=map(int,input().split())

def gcd(a,b):
    while b!=0:
        n=a%b
        a,b=b,n
    return a
print(gcd(n,m))
print(n*m//gcd(n,m))
