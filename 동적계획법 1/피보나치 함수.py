n = int(input())

for i in range(n):
    o = [1, 0]
    z = [0, 1]
    a = int(input())
    for j in range(2,a+1):
        z.append(z[j-1]+z[j-2])
        o.append(o[j-1]+o[j-2])
    print(o[a],z[a])


