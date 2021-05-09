def solve(y,x,maps,p,r,dis):
    global cnt
    if r//2==dis:
        return
    dy=[0,0,-1,1]
    dx=[1,-1,0,0]

    for i in range(4):
        ndy=y+dy[i]
        ndx=x+dx[i]
        if 0<=ndy<len(maps) and 0<=ndx<len(maps[0]):
            if p>=maps[ndy][ndx]:
                cnt+=1
                solve(ndy, ndx, maps, p, r, dis+1)
            else:
                solve(ndy, ndx, maps, p, r, dis+1)
    return cnt
def solution(maps, p, r):
    global cnt
    max_val=0
    answer = 0
    cnt=0
    for i in range(len(maps)):
        for j in range(len(maps[0])):

            solve(i,j,maps,p,r,0)
            max_val=max(cnt,max_val)
            cnt=0

    print(maps)
    print(max_val)
    return answer


maps=[[1, 28, 41, 22, 25, 79, 4],
      [39, 20, 10, 17, 19, 18, 8],
      [21, 4, 13, 12, 9, 29, 19],
      [58, 1, 20, 5, 8, 16, 9],
      [5, 6, 15, 2, 39, 8, 29],
      [39, 7, 17, 5, 4, 49, 5],
      [74, 46, 8, 11, 25, 2, 11]]
p=19
r=6
solution(maps,p,r)