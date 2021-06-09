n=input().split("-")
hap=0

for i in n[0].split("+"):
    hap+=int(i)

for i in n[1:]:
    for j in i.split("+"):
        hap-=int(j)

print(hap)