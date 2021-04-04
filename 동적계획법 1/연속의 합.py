n=int(input())
nums =list(map(int,input().split()))
print(nums)
box=[0]*n

for i in range(n):
    box[i]=max(box[i-1]+nums[i],nums[i])
print(box)