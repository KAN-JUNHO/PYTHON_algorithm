from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer, q = 0, deque()

print(board)
