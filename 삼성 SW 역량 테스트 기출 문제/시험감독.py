N = int(input())
applicant = list(map(int, input().split()))
B, C = map(int, input().split())
answer=0
for num in applicant:
    if num>=B:
        num-=B
        if num % C ==0:
            answer+=num//C
        else:
            answer+= (num//C) +1
print(answer+N)