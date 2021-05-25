n=int(input())
a=4*n-3
star=[[" "]*a for i in range(a)]

def inner(a,idx):
    if a==1:
        star[idx][idx]="*"
        return
    l=4*a-3
    for i in range(idx,l+idx):
        star[idx][i]="*"
        star[idx+l-1][i]="*"

        star[i][idx]="*"
        star[i][idx+l-1]="*"

    inner(a-1,idx+2)
inner(n,0)
for i in star:
    print("".join(i))