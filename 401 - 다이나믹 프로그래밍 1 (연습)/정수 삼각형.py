t=int(input())
tri = [list(map(int,input().split())) for i in range(t)]
tri[1][0]+=tri[0][0]
tri[1][1]+=tri[0][0]
for i in range(2,t):
    for j in range(len(tri[i])):
        if 0<j<len(tri[i-1]):
            tri[i][j]+=max(tri[i-1][j],tri[i-1][j-1])
        elif j==0:
            tri[i][j]+=tri[i-1][j]
        else:
            tri[i][j]+=tri[i-1][j-1]
print(max(tri[-1]))