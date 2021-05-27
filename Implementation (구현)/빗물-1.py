h, w = map(int, input().split(' '))
blocks = list(map(int, input().split(' ')))

answer = 0
for i in range(h):
    first_block = False
    sub_answer = 0
    for j in range(w):
        if not first_block and blocks[j] > i:
            first_block = True
            continue

        if first_block and blocks[j] <= i:
            sub_answer += 1
            continue

        if first_block and blocks[j] > i:
            answer += sub_answer
            sub_answer = 0

print(answer)
