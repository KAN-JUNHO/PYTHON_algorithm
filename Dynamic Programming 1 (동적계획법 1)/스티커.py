t=int(input())
for i in range(t):
    n=int(input())
    stiker=[]
    stiker.append(list(map(int,input().split())))
    stiker.append(list(map(int,input().split())))
    stiker[0][1]+=stiker[1][0]
    stiker[1][1]+=stiker[0][0]

    for j in range(2,n):
        stiker[0][j]+=max(stiker[1][j-2],stiker[1][j-1])
        stiker[1][j]+=max(stiker[0][j-2],stiker[0][j-1])
    print(max(stiker[0][-1],stiker[1][-1]))
