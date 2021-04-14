n=int(input())
m=list(map(str,input()))
stack=[]
box=[]
alpha=[0]*n
for i in range(n):
    alpha[i]=int(input())
for i in m:
    if "A"<=i<="Z":
        num = alpha[ord(i)-ord("A")]
        stack.append(num)
    else:
        arr2=stack.pop()
        arr1=stack.pop()
        if "+"==i:
            a=arr1+arr2
            stack.append(a)
        elif i=="*":
            a=arr1*arr2
            stack.append(a)
        elif i=="-":
            a=arr1-arr2
            stack.append(a)
        elif i=="/":
            a=arr1/arr2
            stack.append(a)
print('%.2f' %stack[0])
