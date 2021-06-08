n=int(input())
box=list(map(int,input().split()))
box.sort()

max_val=box.pop()
for i in range(len(box)):
    max_val+=box[i]/2
print("%g"%max_val)