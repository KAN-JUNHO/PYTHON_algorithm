n=int(input())
box=[int(input()) for i in range(n)]
box.sort()

price=0
while box:
    if len(box)>=3:
        price += box.pop()
        price+=box.pop()
        box.pop()
    else:
        price += box.pop()

print(price)
