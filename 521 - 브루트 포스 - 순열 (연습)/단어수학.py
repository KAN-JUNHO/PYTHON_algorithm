n=int(input())
box=[]
for i in range(n):
    box.append(list(map(str,input())))
print(box)
alpha = [0 for i in range(26)]

for i in box:
    j=0
    while i:
        now=i[-1]
        alpha[ord(now)-ord("A")]+=pow(10,j)
        j+=1
        i.pop()
alpha.sort(reverse=True)
ans=0
for i in range(9,0,-1):
    ans+=i*alpha[9-i]
print(ans)