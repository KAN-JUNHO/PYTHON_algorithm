import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
tmp_sum = 0
min_length = sys.maxsize
while True:
    if s<=tmp_sum:
        min_length=min(min_length,right-left)
        tmp_sum -= arr[left]
        left+=1
    elif right==n:
        break
    else:
        tmp_sum += arr[right]
        right += 1
if min_length==sys.maxsize:
    print(0)
else:
    print(min_length)
