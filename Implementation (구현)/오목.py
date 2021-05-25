n=19
board=[list(map(int,input().split())) for i in range(n)]
white=[[False]*n for _ in range(n)]
black=[[False]*n for _ in range(n)]

def omok(y,x):
    b_c=[]
    w_c=[]
    b_r=[]
    w_r=[]
    for i in range(5):
        if board[y+i][x]:
            b_r.append(black[y+i][x])
            w_r.append(white[y+i][x])

        elif board[y][x+i]:
            b_c.append(black[y][x+i])
            w_c.append(white[y][x+i])
    if all(b_r) or all(b_c):
        return black[y][x]
    elif all(w_r):
        return white[y][x]

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            black[i][j]=True
        elif black[i][j]==2:
            white[i][j]=True

        omok[i][j]