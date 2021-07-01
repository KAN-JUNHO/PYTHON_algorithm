n,a,d=map(int,input().split())
box=list(map(int,input().split()))

cnt=0
for i in range(n):
    if box[i] == a + cnt*d:
        cnt+=1
print(cnt)