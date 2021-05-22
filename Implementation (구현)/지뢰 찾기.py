n=int(input())
mines=[list(input()) for i in range(n)]
check=[list(input()) for i in range(n)]
answer = [['.'] * n for _ in range(n)]

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
def fail():
    global answer
    for i in range(n):
        for j in range(n):
            if mines[i][j] == '*':
                answer[i][j] = '*'
for y in range(n):
    for x in range(n):
        if mines[y][x]=="." and check[y][x]=="x":
            cnt = 0
            for i in range(8):
                ndy=y+dy[i]
                ndx=x+dx[i]
                if 0<=ndy<n and 0<=ndx<n:
                    if mines[ndy][ndx]=="*":
                        cnt+=1
            answer[y][x]=str(cnt)

        if mines[y][x]=="*" and check[y][x]=="x":
            fail()

for i in answer:
    print("".join(i))

