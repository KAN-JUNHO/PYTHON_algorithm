def hanoi(n, frm, mid, to):
    if n==0:
        return
    hanoi(n-1,frm,to,mid)
    print(frm,to)
    hanoi(n-1,mid,frm,to)

n = int(input())
print((2**n)-1)
hanoi(n, 1, 2, 3)