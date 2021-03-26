t = int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    height = n%h
    width = n//h +1
    if height==0:
        height=h
        width-=1
    print(height*100+width)