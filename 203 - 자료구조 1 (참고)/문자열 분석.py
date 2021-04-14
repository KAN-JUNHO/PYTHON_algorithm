import sys

while True:
    n=sys.stdin.readline().rstrip("\n")
    print(n)
    if not n:
        break
    upper_cnt=0
    lower_cnt=0
    space_cnt=0
    digit_cnt=0
    for i in n:
        if i.isupper():
            upper_cnt+=1
        elif i.islower():
            lower_cnt+=1
        elif i.isspace():
            space_cnt+=1
        elif i.isdigit():
            digit_cnt+=1
    print(lower_cnt,upper_cnt,digit_cnt, space_cnt)