k,n=map(int,input().split())
box = [int(input()) for i in range(k)]
def binary(left,right):
    mid=(left+right)//2
    lan=0
    if right < left:
        return right

    for i in box:
        lan+=i//mid
    if lan >= n:
        return binary(mid+1,right)
    else:
        return binary(left,mid-1)

print(binary(1,max(box)))