n=int(input())
box=[]
for i in range(n):
    box.append(list(map(int,str(input()))))
answer=""
def conquer(y,x,n):
    global answer
    for i in range(y,y+n):
        for j in range(x,x+n):
            if box[y][x]!=box[i][j]:
                answer+="("
                conquer(y,x,n//2)
                conquer(y,x+n//2,n//2)
                conquer(y + n // 2, x, n // 2)
                conquer(y + n // 2, x+n//2, n // 2)
                answer += ")"
                return

    if box[y][x]==1:
        answer+="1"
    else:
        answer+="0"
conquer(0,0,n)
print(answer)
