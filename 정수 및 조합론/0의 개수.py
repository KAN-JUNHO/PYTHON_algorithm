n = int(input())
answer = 0

while n>=5:
    answer+= n//5
    n=n//5
print(answer)