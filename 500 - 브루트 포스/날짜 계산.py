import sys

a,b,c=(map(int,sys.stdin.readline().split()))
year=1
while True:
    if (year-a)%15==0 and (year-b)%28==0 and (year-c)%19==0:
        print(year)
        break
    year+=1