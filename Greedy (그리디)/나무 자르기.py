n=int(input())
first=list(map(int,input().split()))
second=list(map(int,input().split()))

hap=sum(first)
second.sort()

for i in range(len(second)):
    hap+=i*second[i]

print(hap)