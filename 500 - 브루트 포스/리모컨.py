n=str(input())
m=int(input())
button = [str(i) for i in range(10)]
box=""
a = list(map(str,input().split()))
for i in a:
    button.remove(i)
click=0
up,down=0,0
dif = abs(int(n)-100)
for i in n:
    if i in button:
        click+=1
        box+=i
    else:
        temp_up=temp_down=int(i)
        click+=1
        while True:
            temp_up=temp_up+1
            temp_down=temp_down-1
            if str(temp_down) in button:
                box+=str(temp_down)
                break
            if str(temp_up) in button:
                box += str(temp_up)
                break
n=int(n)
ans=int(box)
print(min(ans-n+click-1,dif))