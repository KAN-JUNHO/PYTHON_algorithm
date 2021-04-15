
m,n=map(int,input().split())

def factorial_two(n):
    answer_two=0
    while n>=2:
        n=n//2
        answer_two+=n
    return answer_two
def factorial_five(n):
    answer_five=0
    while n>=5:
        n=n//5
        answer_five+=n
    return answer_five
five=factorial_five(m)-factorial_five(m-n)-factorial_five(n)
two=factorial_two(m)-factorial_two(m-n)-factorial_two(n)
print(min(five,two))