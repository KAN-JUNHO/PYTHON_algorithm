import sys
input=sys.stdin.readline
s,e,q=map(str,input().split())

start=int(s[:2])*60+int(s[3:])
end=int(e[:2])*60+int(e[3:])
live=int(q[:2])*60+int(q[3:])

box=dict()
while True:
    try:
        check,name=map(str,input().split())
    except:
        break
    check=int(check[:2])*60+int(check[3:])

    if check<=start:
        if name not in box:
            box[name]=1
    elif end<=check<=live:
        if name in box:
            box[name]+=1
cnt=0
for num in box.values():
    if num>=2:
        cnt+=1

print(cnt)