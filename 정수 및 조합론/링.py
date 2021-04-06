from fractions import Fraction
n= int(input())

ring_list=list(map(int,input().split()))

for i in range(1, n):
    answer = Fraction(ring_list[0],1)/Fraction(ring_list[i],1)
    print(answer.numerator,'/',answer.denominator,sep = '')