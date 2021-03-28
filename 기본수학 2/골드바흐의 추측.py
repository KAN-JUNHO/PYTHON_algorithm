
def prime_list(n):
    sieve = [True]*n
    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i] ==True:
            for j in range(i+i,n,i):
                sieve[j]=False
        return sieve
primes = prime_list(10001)
print(primes)