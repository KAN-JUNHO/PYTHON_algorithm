n=int(input())
box=[int(input()) for  i in range(n)]
box.sort(reverse=True)
ans=0
for i in range(n):
    if box[i]-i>0:
        ans+=box[i]-i

print(ans)