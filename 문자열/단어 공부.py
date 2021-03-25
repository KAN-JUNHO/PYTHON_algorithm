import collections

n = str(input())
n=n.upper()
a= collections.Counter(n)

if (len(a)>1 and a.most_common(2)[0][1]==a.most_common(2)[1][1]):
    print("?")
else:
    print(a.most_common(1)[0][0])