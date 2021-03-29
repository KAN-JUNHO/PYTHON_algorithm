import collections
n = int(input())
box=[]

for i in range(n):
    a = int(input())
    box.append(a)

def mid():
    return (round(sum(box)/n))
def medi():
    if n ==1:
        return box[0]
    box.sort()
    return (box[n//2])
def co():
    a = collections.Counter(box).most_common(2)
    if n>1:
        if a[0][1] == a[1][1]:
            return (a[1][0])
        else:
            return(a[0][0])
    else:
        return(a[0][0])
def ran():
    return (box[-1]-box[0])

print(mid())
print(medi())
print(co())
print(ran())