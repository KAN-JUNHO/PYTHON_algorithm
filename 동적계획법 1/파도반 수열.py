
n = int(input())
box = [1,1,1,2,2]

for _ in range(n):
    a=int(input())
    if len(box)<=a:
        for _ in range(a-len(box)):
            box.append(box[-1]+box[-5])
        print(box[-1])
    else:
        print(box[a-1])