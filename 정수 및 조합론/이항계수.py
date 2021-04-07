n,k = map(int,input().split())

def factorial(n):
	if n==0:
		return 1
	else:
		return factorial(n-1)*n


print(int(factorial(n) / (factorial(k) * factorial(n - k))))