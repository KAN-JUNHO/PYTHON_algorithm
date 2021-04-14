import string
n=input()
n=list(n.upper())
alpha=string.ascii_uppercase
box=len(alpha)*[0]
i=0
while n:
    if alpha[i]==n[0]:
        box[i]+=1
        n.pop(0)
        i=0
        continue
    i+=1
print(*box)