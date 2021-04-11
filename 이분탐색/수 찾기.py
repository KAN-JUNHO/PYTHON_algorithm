n=int(input())
a = list(map(int,input().split()))
m=int(input())
b = list(map(int,input().split()))

a.sort()

def binary(left, right,val):
    if left>right:
        return False
    mid=(left+right)//2
    if a[mid]>val:
        return binary(left,mid-1,val)
    elif a[mid]<val:
        return binary(mid+1,right,val)
    else:
        return True

for i in b:
    if binary(0,n-1,i) == True:
        print(1)
    else:
        print(0)
