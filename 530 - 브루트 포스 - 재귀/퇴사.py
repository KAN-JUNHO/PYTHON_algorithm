n=int(input())
box=[]
for i in range(n):
    t,p=map(int,input().split())
    box.append([t,p])
dp=[0]*n
answer=[]
max_cost=0
def dfs(day,cost):
    global max_cost
    if day==n:
        max_cost = max(max_cost,cost)
        return
    dfs(day+1,cost)
    if day+box[day][0]<=n:
        dfs(day+box[day][0],cost+box[day][1])
dfs(0,0)
print(max_cost)