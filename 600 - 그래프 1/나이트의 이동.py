import collections
def bfs(start_x, start_y):
    que = collections.deque()
    que.append([start_x, start_y])
    while que:
        x, y = que.popleft()
        if x == end_x and y == end_y:
            return board[y][x]
        for i in range(8):
            ndy = y + ny[i]
            ndx = x + nx[i]
            if 0 <= ndy < n and 0 <= ndx < n:
                if board[ndy][ndx]==0:
                    que.append([ndx, ndy])
                    board[ndy][ndx] = board[y][x] + 1
for _ in range(int(input())):
    n=int(input())
    board = [[0] * n for _ in range(n)]
    start_x,start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())
    ny = [2,2,1,1,-1,-1,-2,-2]
    nx = [-1,1,-2,2,-2,2,-1,1]
    print(bfs(start_x,start_y))


