bingo=[list(map(int,input().split())) for i in range(5)]
target=[]
for _ in range(5):
    target.extend(list(map(int,input().split())))
check=[[False]*5 for _ in range(5)]
row=[False]*5
col=[False]*5
line=[False]*2
def bingo_find():
    for i in range(5):
        if all(check[i]):
            row[i]=True
    for i in range(5):
        temp=[]
        for j in range(5):
            temp.append(check[j][i])
        if all(temp):
            col[i]=True

    line_up=[]
    line_down=[]
    for i in range(5):
        line_up.append(check[i][i])
        line_down.append(check[i][4-i])
    if all(line_up):
        line[0]=True
    if all(line_down):
        line[1]=True
def bingo_check():
    cnt=0
    for i in range(5):
        if col[i]:
            cnt+=1
        if row[i]:
            cnt+=1
    for i in range(2):
        if line[i]:
            cnt+=1
    return cnt

for i in range(len(target)):
    y=None
    for j in range(5):
        if target[i] in bingo[j]:
            y=j
            break
    x = bingo[y].index(target[i])
    check[y][x]=True
    bingo_find()
    if bingo_check() >= 3:
        print(i+1)
        break