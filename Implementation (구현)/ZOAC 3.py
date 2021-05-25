a,b = map(str,input().split())
n=input()
keyword=["qwertyuiop","asdfghjkl","zxcvbnm"]
left=["qwert","asdfg","zxcv"]
right=["yuiop","hjkl","bnm"]

for i in range(len(left)):
    if a in left[i]:
        y1 = i
        x1 = keyword[i].index(a)
        break
for i in range(len(right)):
    if b in right[i]:
        y2 = i
        x2 = keyword[i].index(b)
        break
time=0
for string in n:
    time+=1
    for i in range(3):
        if string in left[i]:
            y=i
            x=keyword[i].index(string)
            time+=abs(x1-x)+abs(y1-y)
            x1=x
            y1=y
            break
        elif string in right[i]:
            y = i
            x = keyword[i].index(string)
            time += abs(x2 - x) + abs(y2 - y)
            x2 = x
            y2 = y
            break
print(time)