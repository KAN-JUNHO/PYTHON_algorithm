import string
n=input()
n=list(n.lower())
alpha=list(string.ascii_lowercase)
box=len(alpha)*[-1]
    
for i in range(len(n)):
    if box[alpha.index(n[i])]==-1:
        box[alpha.index(n[i])]=i
print(*box)