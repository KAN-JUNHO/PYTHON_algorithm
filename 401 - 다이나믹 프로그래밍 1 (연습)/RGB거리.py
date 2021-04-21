n=int(input())
paints=[]
for i in range(n):
    paints.append(list(map(int,input().split())))
for i in range(1,n):
    paints[i][0]=min(paints[i-1][1],paints[i-1][2])+paints[i][0]
    paints[i][1]=min(paints[i-1][0],paints[i-1][2])+paints[i][1]
    paints[i][2]=min(paints[i-1][0],paints[i-1][1])+paints[i][2]
print(min(paints[-1]))
