import string
n,b=map(int,input().split())
alpha=list(string.ascii_uppercase)
for i in range(0,10):
    alpha.insert(i,str(i))
answer=""
while n:
    answer+=alpha[n%b]
    n=n//b
print(answer[::-1])
