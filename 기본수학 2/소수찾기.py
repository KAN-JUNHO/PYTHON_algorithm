n= int(input())
numbers = map(int,input().split())
cnt=0
for number in numbers:
    if number>1:
        for i in range(2,number):
            if number % i == 0:
                break
        else:
            cnt+=1
print(cnt)