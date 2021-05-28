n=input()
max_v=0
min_v=10e9
def odd_cnt(n):
    odd=0
    for i in n:
        if int(i)%2==1:
            odd+=1
    return odd
def solve(n,odd):
    global max_v,min_v
    if len(n)==1:
        max_v=max(odd,max_v)
        min_v=min(odd,min_v)
    elif len(n)==2:
        temp=str(int(n[0])+int(n[1]))
        solve(temp,odd+odd_cnt(temp))

    for i in range(len(n)-2):
        for j in range(i+1,len(n)-1):
            a=n[:i+1]
            b=n[i+1:j+1]
            c=n[j+1:]
            temp=str(int(a)+int(b)+int(c))
            solve(temp,odd+odd_cnt(temp))


solve(n,odd_cnt(n))
print(min_v,max_v)