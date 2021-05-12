import sys
n,m=map(int,input().split())

box_name={}
box_number={}

for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    box_number[i]=name
    box_name[name]=i

for _ in range(m):
    find = sys.stdin.readline().strip()
    if find.isdigit() :
        print(box_number[int(find)])
    else:
        print(box_name[find])