N=int(input())
res=""
while N:
    if N%(-2):
        res = '1' + res
        N = N//-2 + 1
    else:
        res = '0' + res
        N //= -2
print(res)