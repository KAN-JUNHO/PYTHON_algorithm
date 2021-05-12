n=int(input())
box = input()
nums = [int(input()) for i in range(n)]

stack=[]
for i in box:
    if i.isalpha():
        stack.append(nums[ord(i)-ord("A")])
    else:
        num2=stack.pop()
        num1=stack.pop()
        stack.append(str(eval(str(num1)+i+str(num2))))
print(format(float(stack[0]), '.2f'))