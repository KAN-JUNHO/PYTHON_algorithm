a=input()
dial = {('A', 'B', 'C'):2,
        ('D','E','F'):3,
        ('G','H','I'):4,
        ('J','K','L'):5,
        ('M','N','O'):6,
        ('P','Q','R','S'):7,
        ('T','U','V'):8,
        ('W','X','Y','Z'):9}
count=0
for i in a:
    for key in dial:
        if i in key:
            count+=(dial[key]+1)
print(count)