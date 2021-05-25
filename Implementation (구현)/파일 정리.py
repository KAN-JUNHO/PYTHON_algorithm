n=int(input())
box=[]
for i in range(n):
    a=input()
    for j in range(len(a)):
        if a[j]==".":
            box.append(a[j+1:])
dic={}
for i in box:
    if i not in dic:
        dic[i]=0
    dic[i]+=1
a = sorted(dic.items())


for key,value in a:
    print(key,value)