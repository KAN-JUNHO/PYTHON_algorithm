n=19
board=[list(map(int,input().split())) for i in range(n)]
dx=[0,1,1,1]
dy=[1,0,1,-1]
def mok():
    for j in range(n):
        for i in range(n):
            if board[j][i]:
                for k in range(4):
                    move_y = j
                    move_x = i
                    cnt = 1
                    while 0<=move_y+dy[k]<n and 0<=move_x+dx[k]<n and (board[j][i]==board[move_y+dy[k]][move_x+dx[k]]):
                        move_y += dy[k]
                        move_x += dx[k]
                        cnt+=1
                    if cnt==5:
                        move_y=j
                        move_x=i
                        if 0<=move_y-dy[k]<n and 0<=move_x-dx[k]<n and board[j][i]==board[move_y-dy[k]][move_x-dx[k]]:
                            break
                        else:
                            return board[j][i],j+1,i+1
    else:
        return 0,-1,-1
c,y,x=mok()
if c==0:
    print(0)
else:
    print(c)
    print(y,x)


