def solution(numbers):

    num=["0","1","2","3","4","5","6","7","8","9"]
    box=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer=dict(list(zip(num,box)))

    numbers=list(map(str,numbers))
    change=[]
    for i in numbers:
        alpha=""
        for idx in i:
            if idx in answer:
                alpha+=answer[idx]
        change.append(alpha)
    print(change)
    change.sort()
    ans=[]
    for i in change:
        for j in answer.items():
            alpha = ""
            if j[1] in i:
                while len(i)!=0:
                    alpha+=j[0]
                    i=i[len(j[1]):]
                ans.append(alpha)
    ans=list(map(int,ans))
    print(ans)
solution([4, 5, 11])