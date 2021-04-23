n=int(input())
paint = [list(map(int,input().split())) for i in range(n)]
for i in range(1,n):
    paint[i][0]=paint[i][0]+min(paint[i-1][1],paint[i-1][2])
    paint[i][1]=paint[i][1]+min(paint[i-1][0],paint[i-1][2])
    paint[i][2]=paint[i][2]+min(paint[i-1][0],paint[i-1][1])

print(paint)