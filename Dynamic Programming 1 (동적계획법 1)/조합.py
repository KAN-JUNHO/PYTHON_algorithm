import math
n,m=map(int,input().split())
answer=(math.factorial(n)//(math.factorial(m)*math.factorial(n-m)))
print(answer)