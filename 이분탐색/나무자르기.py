import sys
n,m = map(int,sys.stdin.readline().split())
box = list(map(int,sys.stdin.readline().split()))

def binary(left,right):
    mid=(left+right)//2
    if left>right:
        return right
    hap=0
    for i in box:
        if i>mid:
            hap+=i-mid
    if hap>=m:
        return binary(mid+1,right)
    elif hap<m:
        return binary(left,mid-1)

print(binary(1,max(box)))