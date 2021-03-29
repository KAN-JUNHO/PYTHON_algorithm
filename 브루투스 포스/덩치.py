n = int(input())
box=[]
for i in range(n):
    a,b= (map(int, input().split()))
    box.append([a,b])
for i in range(len(box)):
    rank=1
    for j in range(len(box)):
        if box[i][0]<box[j][0] and box[i][1] < box[j][1]:
            rank+=1
    print(rank)