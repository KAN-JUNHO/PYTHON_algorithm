n= int(input())
words = [input().split() for i in range(n)]
ans=[]
for i in range(n):
    for i in words[i]:
        ans.append(i[::-1])
    print(*ans)
    ans.clear()
