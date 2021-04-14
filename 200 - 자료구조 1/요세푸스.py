n,k = map(int,input().split())
nums = [i for i in range(1,n+1)]
stack=[]
i=k-1
while nums:
    if len(nums)-1 < i:
        i=i-len(nums)
    else:
        stack.append(nums[i])
        del nums[i]
        i+=k-1
print("<%s>" % (", ".join(map(str,stack))))