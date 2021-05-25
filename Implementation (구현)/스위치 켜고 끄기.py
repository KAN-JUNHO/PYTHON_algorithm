n=int(input())
switch=list(map(int,input().split()))
students=int(input())
for _ in range(students):
    gen,num=map(int,input().split())
    if gen==1:
        for i in range(len(switch)):
            if (i+1)%num==0:
                if switch[i]:
                    switch[i]=0
                else:
                    switch[i]=1
    else:
        if switch[num-1]:
            switch[num-1]=0
        else:
            switch[num-1]=1
        left,right=num-2,num
        while 0<=left and right<n and switch[left]==switch[right]:
            if switch[left]:
                switch[left]=0
            else:
                switch[left]=1
            if switch[right]:
                switch[right]=0
            else:
                switch[right]=1
            left-=1
            right+=1

for i in range(0,len(switch),10):
    print(*switch[i:i+10])