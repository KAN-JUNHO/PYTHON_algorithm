from collections import deque
n=int(input())
box=input()
ans=10e9

red=deque(box[:])
blue=deque(box[:])

cnt_b=1
cnt_r=1


while blue:
    if blue[0] == "R":
        while len(blue)>1 and blue[0] == blue[1]:
            blue.popleft()
        else:
            blue.popleft()
            cnt_b+=1
    else:
        blue.popleft()
while red:
    if red[0] == "B":
        while len(red)>1 and red[0] == red[1]:
            red.popleft()
        else:
            red.popleft()
            cnt_r+=1
    else:
        red.popleft()

ans=min(cnt_r,cnt_b)
print(ans)

