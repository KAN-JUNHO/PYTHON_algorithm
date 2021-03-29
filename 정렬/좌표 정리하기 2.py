n = int(input())
box=[]
for i in range(n):
    box.append(list(map(int,input().split())))

box.sort(key=lambda x:(x[1],x[0]))
for i,j in box:
    print(i,j)