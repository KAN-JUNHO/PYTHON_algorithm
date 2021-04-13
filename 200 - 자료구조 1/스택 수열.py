n=int(input())

stack=[]
box=[]
arr=[]
answer=''
for i in range(1,n+1):
    box.append(int(input()))
    arr.append(i)
while arr or stack:
    if stack and stack[-1]==box[0]:
        del stack[-1]
        del box[0]
        answer+="-"
    elif arr and arr[0]<=box[0]:
        stack.append(arr[0])
        del arr[0]
        answer+="+"
    else:
        break

if stack:
    print("NO")
else:
    for i in answer:
        print(i)