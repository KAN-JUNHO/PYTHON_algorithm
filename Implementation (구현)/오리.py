duck=input()
if len(duck) % 5 != 0:
    print(-1)
    exit()
def solve(index):
    global cnt
    start=True
    quack = "quack"
    j=0
    for i in range(index,len(duck)):
        if quack[j]==duck[i] and not check[i]:
            check[i]=True
            if duck[i]=="k":
                if start:
                    cnt+=1
                    start=False
                j=0
                continue
            j+=1
check=[False]*len(duck)
cnt=0
for i in range(len(duck)):
    if duck[i]=="q" and check[i]==False:
        solve(i)

if cnt==0 or not all(check):
    print(-1)
else:
    print(cnt)