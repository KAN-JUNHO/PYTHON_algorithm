n = int(input())
box=[]
for i in range(n):
    a = list(map(int,input().split()))
    box.append(a)
box.sort(key=lambda x:(x[0],x[-1]))
for i,j in box:
    print(i,j)