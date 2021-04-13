n = int(input())
box=[]
num=[]
cnt=0
for i in range(1,n+1):
    num.append(int(input()))
    box.append(i)
check=True
ans=[]
stack=[]
for i in range(n):
    while box and num[0]>=box[0]:
        stack.append(box.pop(0))
        ans.append("+")
    if num and num[0]==stack[-1]:
        stack.pop()
        num.pop(0)
        ans.append("-")
    else:
        check=False
        break
if check==False:
    print("NO")
else:
    for i in ans:
        print(i)