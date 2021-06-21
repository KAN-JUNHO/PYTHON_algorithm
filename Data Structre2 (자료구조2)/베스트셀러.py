n=int(input())
books=dict()

for i in range(n):
    book=input()
    if book in books:
        books[book]+=1
    else:
        books[book]=1
books=sorted(books.items(),key=lambda x:(-x[1],x[0]))

print(books[0][0])
