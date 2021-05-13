import collections
import sys

box=collections.defaultdict(int)
total=0
while True:
    a=sys.stdin.readline().strip()
    if a=="":
        break
    box[a]+=1
    total+=1
name=list(box.keys())
name.sort()
for i in name:
    print(i,format(box[i]*100/total,".4f"))