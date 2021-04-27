n=int(input())
length=len(str(n))
hap=0
for i in range(length-1):
    hap+=9*(10**i)*(i+1)
hap+=((n-(10**(length-1))+1)*(length))
print(hap)