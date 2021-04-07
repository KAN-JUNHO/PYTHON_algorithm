from collections import Counter

n=int(input())

for i in range(n):
    m=int(input())
    cloth=[]
    for j in range(m):
        a=list(map(str,input().split()))
        cloth.append(a[1])

    result=Counter(cloth)
    num=1
    for i in result:
        num *= result[i] + 1
    print(num - 1)
