a = int(input())
cnt=0
while 0<=a:
    a -= cnt
    cnt += 1
print(a,cnt)
a = cnt+a-1
print(a)

