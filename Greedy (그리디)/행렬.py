N, M = list(map(int, input().split()))
map_list = [list(map(int, list(input()))) for _ in range(N)]
wanted_list = [list(map(int, list(input()))) for _ in range(N)]

cnt = 0
def check():
    for i in range(N):
        for j in range(M):
            if map_list[i][j] != wanted_list[i][j]:
                return False
    return True
def solve(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            map_list[i][j] = 1 - map_list[i][j]
for i in range(0, N-2):
    for j in range(0, M-2):
        if map_list[i][j] != wanted_list[i][j]:
            cnt += 1
            solve(i, j)
if check():
    print(cnt)
else:
    print(-1)
