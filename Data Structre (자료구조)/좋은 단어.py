n=int(input())
cnt=0
for _ in range(n):
    stack=[]
    word=input()

    for i in word:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)

    if not stack:
        cnt+=1
print(cnt)