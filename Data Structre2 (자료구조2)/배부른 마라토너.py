import sys
from collections import defaultdict
n=int(sys.stdin.readline())
start=defaultdict(int)

for i in range(n):
    start[sys.stdin.readline()]+=1
for i in range(n-1):
    start[sys.stdin.readline()]-=1

for i in start:
    if start[i]:
        print(i)
        break