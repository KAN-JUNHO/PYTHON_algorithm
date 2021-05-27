n=input()
min_v=10e9
max_v=0

def odd_cnt(n):
    odd_n=0
    for i in n:
        if int(i)%2==1:
            odd_n+=1
    return odd_n

def solve(n,odd_n):
    global min_v,max_v
    if len(n)==1:
        min_v=min(min_v,odd_n)
        max_v=min(min_v,odd_n)
    elif len(n)==2:
        temp=str(int(n[0])+int(n[1]))
        solve(temp,odd_n+odd_cnt(temp))
    else:
        for i in range(len(n)-2):
            for j in range(i+1,len(n)-1):
                a=n[:i+1]
                b=n[i+1:j+1]
                c=n[j+1:]
                temp=str(int(a)+int(b)+int(c))
                solve(temp,odd_n+odd_cnt(temp))

solve(n,odd_cnt(n))
print(min_v,max_v)