a=list(map(int,input().split()))
arr1=[]
arr2=[]
for i in range(a[0]):
    arr1.append(list(map(int,input().split())))
a=list(map(int,input().split()))
for i in range(a[0]):
    arr2.append(list(map(int, input().split())))

answer=[]
for i in range(len(arr1)):
    w=[]
    for j in range(len(arr2[0])):
        v=0
        for k in range(len(arr1[0])):
            v += arr1[i][k] * arr2[k][j]
        w.append(v)
    answer.append(w)

for i in answer:
    print(*i)