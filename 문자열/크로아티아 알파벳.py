a=input()
cnt=0
b= ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in b:
    if i in a:
        a = a.replace(i,"!")

print(len(a))