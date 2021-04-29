n=int(input())
box = [list(map(int,input().split())) for i in range(n)]
ans=[]
check=[False]*n
team=[]
for i in range(n):
    for j in range(n):
        if i!=j and check[i]==False and check[j]==False:
            ans.append(box[i][j]+box[j][i])
            check[j]=True
            check[i]=True
    else:
        if all(check):
            team.append(ans[:])
            ans.clear()
            check = [False] * n

print(team)