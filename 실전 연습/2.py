from collections import deque
def bfs(p,y,x,cnt):
    visted=[[False]*5 for i in range(5)]
    que = deque()
    que.append([p,y,x,cnt])
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    visted[y][x]=True
    while que:
        p,y,x,cnt = que.popleft()
        if cnt>2:
            return 1
        for i in range(4):
            ndy=dy[i]+y
            ndx=dx[i]+x
            if 0<=ndy<5 and 0<=ndx<5 and visted[ndy][ndx]==False:
                cnt+=1
                if places[p][ndy][ndx]=="O":
                    que.append((p,ndy,ndx,cnt))
                elif places[p][ndy][ndx]=="P":
                    return 0
                visted[ndy][ndx]=True
    else:
        return 1
def solution(places):
    check=False
    answer = []
    for i in range(len(places)):
        for j in range(5):
            if check==True:
                check=False
                break
            for k in range(5):
                if places[i][j][k]=="P":
                    start_y,start_x=j,k
                    a=bfs(i, j, k, 0)
                    if a==0:
                        answer.append(a)
                        check=True
                        break
        else:
            answer.append(a)

    print(answer)
    return answer

places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)
