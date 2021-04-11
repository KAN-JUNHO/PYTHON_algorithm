n=int(input())
box=[list(map(int,str(input()))) for i in range(n)]
white=0
black=0
answer=""
def conquer(y, x, n):
    global answer
    for i in range(y,y+n):
        for j in range(x,x+n):
            if box[y][x] != box[i][j]:
                k=n//2
                answer+="("
                conquer(y,x,k)
                conquer(y,x+k,k)
                conquer(y+k,x,k)
                conquer(y+k,x+k,k)
                answer+=")"
                return

    if box[y][x]==1:
        answer+="1"
    else:
        answer+="0"
conquer(0,0,n)
print(answer)
