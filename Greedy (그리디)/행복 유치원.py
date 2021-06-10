n, k = map(int, input().split())
person = list(map(int, input().split()))

diff=[]

for i in range(n-1):
    diff.append(abs(person[i]-person[i+1]))
diff.sort()

if k==n:
    print(0)
else:
    print(sum(diff[:n-k]))

