import string
n,b=map(str,input().split())
b=int(b)
alpha=list(string.ascii_uppercase)
for i in range(0,10):
    alpha.insert(i,str(i))
answer=0
for i,j in enumerate(n[::-1]):
    answer+=alpha.index(j)*(b**i)

print(answer)