import math
m,n = map(int,input().split())
for i in range(m,n+1):
    if i>1:
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
               print(i)