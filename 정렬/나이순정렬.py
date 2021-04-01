n = int(input())
box=[]
for i in range(n):
    age,name = (map(str,input().split()))
    age = int(age)
    box.append([age,name,i])
box.sort(key=lambda x:(x[0],x[2]))
for i in box:
    print(i[0],i[1])


