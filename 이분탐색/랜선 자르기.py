
k,n =map(int,input().split())
lan = [int(input()) for i in range(k)]

def binary(left,right):
    mid =(left+right)//2
    if right<left:
        return right
    lines=0
    for i in lan:
        lines+= i //mid
    if lines >=n:
        return binary(mid+1,right)
    else:
        return binary(left,mid-1)

print(binary(1,max(lan)))
