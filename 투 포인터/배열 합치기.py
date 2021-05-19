n,m=map(int,input().split())
box=[]

box.extend(map(int, input().split()))
box.extend(map(int,input().split()))
box.sort()
print(*box)