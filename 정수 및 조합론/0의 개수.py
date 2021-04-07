n = int(input())
answer = 0
if n<5:
    print(0)
else:
    while n!=1:
        n//=5
        answer+=n
    print(answer)