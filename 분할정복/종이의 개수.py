n=int(input())
box=[]
for i in range(n):
    box.append(list(map(int,input().split())))

minus,plus,zero=0,0,0
def conquer(x, y, n):
    global minus,plus,zero

    for i in range(x, x + n):
        for j in range(y,y+n):
            if box[y][x]!=box[j][i]:
                k=n//3
                conquer(x, y, k)
                conquer(x + k, y, k)
                conquer(x + 2*k, y, k)
                conquer(x, y + k, k)
                conquer(x + k,  y+ k, k)
                conquer(x + 2*k, y + k, k)
                conquer(x, y + 2*k, k)
                conquer(x + k, y + 2*k, k)
                conquer(x + 2*k, y + 2*k, k)
                return
    if box[y][x]==-1:
        minus+=1
    elif box[y][x]==0:
        zero+=1
    else:
        plus+=1

conquer(0,0,n)
print(minus)
print(zero)
print(plus)
#5940 15301 12420