n=int(input())
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

for i in range(n):
    hap = 0
    box=list(map(int,input().split()))
    a=box.pop(0)
    for j in range(a):
        for k in range(j+1,a):
            hap+=gcd(box[j],box[k])
    print(hap)
