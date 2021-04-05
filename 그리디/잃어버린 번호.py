import re
n=str(input())
n=re.split("([+-])",n)
for i in range(len(n)):
    while n[i][0]=="0":
        n[i]=n[i][1:]

while "+" in n:
    i=n.index("+")
    n[i-1]=eval(str(n[i-1])+str(n[i])+str(n[i+1]))
    del n[i]
    del n[i]

while "-" in n :
    i=n.index("-")
    n[i - 1] = eval(str(n[i - 1]) + str(n[i]) + str(n[i + 1]))
    del n[i]
    del n[i]

    if len(n)==1:
        break
print(n[0])
