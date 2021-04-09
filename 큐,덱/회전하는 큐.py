from collections import deque
n,m = map(int,input().split())
nums = deque(list(map(int,input().split())))
que =deque(i for i in range(1,n+1))

cnt=0
while nums:
    if nums[0]==que[0]:
        nums.popleft()
        que.popleft()
    else:
        if que.index(nums[0])<=len(que)//2:
            while que[0] != nums[0]:
                que.append(que.popleft())
                cnt+=1
        else:
            while que[0] != nums[0]:
                que.appendleft(que.pop())
                cnt+=1
print(cnt)