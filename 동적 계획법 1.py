n = int(input())
c0=[1,0]
c1=[0,1]

for i in range(n):
    a = int(input())
    for j in range(2,a+1):
        c0.append(c0[j-1]+c0[j-2])
        c1.append(c1[j-1]+c1[j-2])

    print(c0[a],c1[a])

