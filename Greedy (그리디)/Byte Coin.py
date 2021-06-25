n,w=map(int,input().split())
price=[int(input()) for i in range(n)]

coin=0
for i in range(1,n):
    if price[i-1]<=price[i]:
        coin+=w//price[i-1]
        w=w%price[i-1]
    else:
        w+=coin*price[i-1]
        coin=0

print(w+coin*price[-1])