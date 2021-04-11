n=int(input())
box=[list(map(int,input().split())) for i in range(n)]
blue=0
white=0

def conquer(y, x, n):
    global blue,white
    for i in range(x,x+n):
        for j in range(y,y+n):
            if box[y][x] != box[j][i]:
                k=n//2
                conquer(y,x,k)
                conquer(y+k,x,k)
                conquer(y,x+k,k)
                conquer(y+k,x+k,k)
                return
    if box[y][x]==1:
        blue+=1
    else:
        white+=1

conquer(0,0,n)
print(white)
print(blue)
