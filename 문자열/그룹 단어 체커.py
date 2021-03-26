import collections
n = int(input())
cnt=0
for i in range(n):
    a = input()
    for j in range(len(a)-1):
        if a[j] in a[j+1]:
            continue
        elif a[j] in a[j+2:]:
            break
    else:
        cnt+=1

print(cnt)