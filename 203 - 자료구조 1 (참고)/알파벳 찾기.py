import string
n=input()
n=list(n.lower())
alpha=list(string.ascii_lowercase)
box=len(alpha)*[0]

for i in range(len(alpha)):
    for j in range(len(n)):
        if alpha[i]==n[j]:
            box[i]=j
            break
    else:
        box[i]=-1
print(*box)