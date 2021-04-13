n=int(input())
box = [list(map(int,input().split(" "))) for i in range(n)]
zero,minuse,plus=0,0,0
def conquer(y,x,n):
    global minuse, zero, plus
    for i in range(y,y+n):
        for j in range(x,x+n):
            if box[y][x]!=box[i][j]:
                k=n//3
                conquer(y,x,k)
                conquer(y,x+k,k)
                conquer(y,x+(2*k),k)
                conquer(y+k,x,k)
                conquer(y+k,x+k,k)
                conquer(y+k,x+(2*k),k)
                conquer(y+(2*k),x,k)
                conquer(y + (2 * k), x+k, k)
                conquer(y + (2 * k), (x+2*k), k)
                return 
    if box[y][x]==-1:
        minuse+=1
    elif box[y][x]==0:
        zero+=1
    else:
        plus+=1
conquer(0,0,n)
print(minuse)
print(zero)
print(plus)