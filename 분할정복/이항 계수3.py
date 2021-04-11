
n,k=map(int,input().split())

def factorial(v):
    if v==1:
        return 1
    return factorial(v-1)*v
a=factorial(n)//(factorial(k)*(factorial(n-k)))
print(a%1000000007)
