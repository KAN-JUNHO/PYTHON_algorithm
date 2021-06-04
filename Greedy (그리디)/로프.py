n=int(input())
box=[]
for i in range(n):
    box.append(int(input()))
box.sort(reverse=True)
ans=0
for i in range(1,n+1):
    ans=max(box[i-1]*i,ans)
print(ans)