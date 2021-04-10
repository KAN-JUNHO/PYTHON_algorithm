import sys
from collections import deque


T = int(sys.stdin.readline())

for _ in range(T):
    operation = input()
    n = int(sys.stdin.readline())
    temp = input()
    temp = temp[1:-1]

    if "," not in temp and temp != "":
        num_deque = deque([int(temp)])
    elif temp != "":
        num_deque = deque(map(int, temp.split(",")))
    else:
        num_deque = deque()

    flag = 1
    cnt = 0

    for i in range(len(operation)):
        if operation[i] == "R":
            cnt += 1
        else:
            if len(num_deque) == 0:
                flag = 0
                break

            if cnt % 2 == 0:
                num_deque.popleft()
            else:
                num_deque.pop()
    if cnt % 2 == 1:
        num_deque.reverse()

    if flag:
        num_deque = list(map(str,num_deque))
        print("[", end="")
        print(",".join(num_deque), end="")
        print("]")
    else:
        print("error")