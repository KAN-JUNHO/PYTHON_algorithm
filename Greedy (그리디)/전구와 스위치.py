n=int(input())
a=list(map(int,input()))
b=list(map(int,input()))


def change(number):
    if number==0:
        return 1
    else:
        return 0

def switch(temp,cnt):

    if cnt==1:
        temp[0]=change(temp[0])
        temp[1]=change(temp[1])
    for i in range(1,n):
        if temp[i-1]!=b[i-1]:
            cnt+=1
            temp[i-1] = change(temp[i-1])
            temp[i] = change(temp[i])
            if i==n-1:
                 continue
            temp[i+1]=change(temp[i+1])
    if temp==b:
        return cnt
    else:
        return -1
first_on=switch(a[:],1)
first_off=switch(a[:],0)

if first_on>=0 and first_off>=0:
    print(min(first_on,first_off))
elif first_on>=0 and first_off<0:
    print(first_on)
elif first_on<0 and first_off>=0:
    print(first_off)
else:
    print(-1)