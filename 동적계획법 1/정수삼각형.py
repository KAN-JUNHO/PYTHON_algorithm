n = int(input())
box =[list(map(int,input().split())) for i in range(n)]

for i in range(1,n):
    for j in range(len(box[i])):
        if j==0:
            box[i][0]+=box[i-1][0]
        elif i==j:
            box[i][-1]+=box[i-1][-1]
        else:
            box[i][j] += max(box[i-1][j],box[i-1][j-1])

print(max(box[n-1]))