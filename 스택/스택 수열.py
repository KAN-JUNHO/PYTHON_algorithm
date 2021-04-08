n=int(input())
box=[]
arr=[]
for i in range(1,n+1):
    box.append(i)
    arr.append(int(input()))
stack=[]

ans =[]
while len(arr)!=0:
    while (stack and arr and arr[0]==stack[-1]) or (box[0]!=arr[0]):

        if stack and arr and arr[0]==stack[-1]:
            print("-")
            ans.append(stack.pop())
            arr.pop(0)
        elif box[0]!=arr[0]:
            print("+")
            stack.append(box.pop(0))
    else:
        ans.append(box[0])
        box.pop(0)
        arr.pop(0)