
t = int(input())
def factorial(n):
    if n<=1:
        return 1
    else:
        return factorial(n-1)*n
for _ in range(t):
    k,n = map(int,input().split())
    a=factorial(n)//(factorial(k)*factorial(n-k))
    print(a)