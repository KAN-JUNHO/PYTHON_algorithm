from collections import Counter

n = int(input())

for i in range(n):
    box = []
    for j in range(int(input())):
        a,b=map(str,input().split())
        box.append(b)
    cnt = Counter(box)
    v=1
    for j in cnt.values():
        v*=(j+1)
    print(v-1)

