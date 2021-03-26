a,b,v = map(int,input().split())
day = (v-b)/(a-b)
if day%1!=0:
    day+=1

day = int(day)
print(day)