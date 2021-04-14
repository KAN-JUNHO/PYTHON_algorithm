import string
import sys

n=sys.stdin.readline().rstrip()
answer=''
A=list(string.ascii_uppercase)
a=list(string.ascii_lowercase)

for i in range(len(n)):
    if n[i].isalpha():
        if n[i].isupper():
            B=A.index(n[i])+13
            if B<26:
                answer+=A[B]
            else:
                B=B-26
                answer+=A[B]
        elif n[i].lower():
            b=a.index(n[i])+13
            if b<26:
                answer+=a[b]
            else:
                b-=26
                answer+=a[b]
    else:
        answer+=n[i]
print(answer)