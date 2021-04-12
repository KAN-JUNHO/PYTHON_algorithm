m,n = map(int,input().split())
house = [int(input()) for i in range(m)]
house.sort()

left=1
right=house[-1]-house[0]
answer=0
def house_cnt(dis):
    cur_house = house[0]
    cnt=1
    for i in range(1,m):
        if cur_house+dis <= house[i]:
            cnt+=1
            cur_house=house[i]
    return cnt
def binary(left,right):
    global answer
    mid = (left+right)//2
    if right<left:
        return answer

    if house_cnt(mid) >= n:
        answer=mid
        return binary(mid+1,right)
    else:
        return binary(left,mid-1)


print(binary(left,right))