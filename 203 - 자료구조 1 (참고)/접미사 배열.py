n=input()
box=[]
for i in range(len(n)):
    box.append(n[i:])
box.sort()
for i in box:
    print(i)