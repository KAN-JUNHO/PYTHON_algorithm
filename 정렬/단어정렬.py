n = int(input())
words=[]
for i in range(n):
    word=str(input())
    if not word in words:
        words.append(word)
words.sort(key=lambda x:(len(x),x))
for i in words:
    print(i)