a = int(input())

def fact(a):
    if a==0:
        return 1

    return a*fact(a-1)

ans = fact(a)
print(ans)