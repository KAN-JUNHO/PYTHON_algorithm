
box=[]
while True:
    a,b= list(map(int,input().split()))
    if a==0 and b==0:
        break
    else:
        box.append([a,b])


for i,j in box:
    if j % i ==0:
        print("factor")
    elif i % j ==0:
        print("multiple")
    else:
        print("neither")