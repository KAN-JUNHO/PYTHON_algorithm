

n=int(input())
box = [list(map(int,input().split())) for i in range(n)]


def conquer(y, x, n):
    global white,blue
    for i in range(y,y+n):
        for j in range(x,x+n):
            if box[y][x] != box[i][j]:
                conquer(y,x,n//2)
                conquer(y,x+n//2,n//2)
                conquer(y+n//2,x,n//2)
                conquer(y+n//2,x+n//2,n//2)
                return

    if box[y][x]==1:
        blue+=1
    else:
        white+=1
white=0
blue=0
conquer(0,0,n)
print(white)
print(blue)
