n,c= map(int,input().split())
box=[int(input()) for i in range(n)]
box.sort()
print(box)
left = 1
right = box[-1]-box[0]

def cnt(mid):
    count=1
    cur_=box[0]
    for i in range(1,n):
        if cur_+mid <= box[i]:
            count+=1
            cur_=box[i]
    return count
def binary(mi,ma):
    global answer
    if ma< mi:
        return answer
    mid = (mi+ma)//2
    if cnt(mid)>=c:
        answer=mid
        return binary(mid+1,ma)
    else:
        return binary(mi,mid-1)

print(binary(left,right))