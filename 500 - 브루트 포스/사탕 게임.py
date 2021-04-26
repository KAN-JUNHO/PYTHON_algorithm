n=int(input())
box = [list(map(str,input())) for i in range(n)]
def checkrow():
    maxNum = 1
    for i in range(0,n):
        cnt = 1
        for j in range(1, n):
            if (box[i][j] == box[i][j - 1]):
                cnt += 1
                maxNum = max(maxNum, cnt)
            else: cnt = 1
    return maxNum
def checkcol():
    maxNum = 1
    for j in range(0, n):
        cnt = 1
        for i in range(1, n):
            if (box[i][j] == box[i-1][j]):
                cnt += 1
                maxNum = max(maxNum, cnt)
            else: cnt = 1
    return maxNum

a=0
for i in range(n):
    for j in range(n):
        if j<n-1 and box[i][j]!=box[i][j+1]:
            temp=box[i][j]
            box[i][j],box[i][j+1] = box[i][j+1],temp
            a=max(a,checkrow(),checkcol())
            box[i][j], box[i][j + 1] = temp, box[i][j]
        if i<n-1 and box[i][j]!=box[i+1][j]:
            temp = box[i][j]
            box[i][j], box[i+1][j] = box[i+1][j], temp
            a = max(a,checkrow(),checkcol())
            box[i][j], box[i+1][j] = temp,box[i][j]
print(a)