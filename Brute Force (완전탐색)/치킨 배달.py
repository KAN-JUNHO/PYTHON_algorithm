n,m=map(int,input().split())
city=[list(map(int,input().split())) for i in range(n)]
print(city)
chicken=[]
home=[]
for i in range(n):
    for j in range(n):
        if city[i][j]==2:
            chicken.append([i,j])
