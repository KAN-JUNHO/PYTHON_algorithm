n=int(input())
ans=[]

for i in range(n//2):
    ans.extend([1,2])
if n%2==1:
    ans.append(3)
print(*ans)