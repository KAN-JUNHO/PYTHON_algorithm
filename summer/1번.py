def solution(code, day, data):
    answer = []
    ans=[]
    for i in data:
        answer.append(i.split())
    answer.sort(key=lambda x : x[2])
    print(answer)
    for i in answer:
        if code in i[1] and day in i[2]:
            ans.append(int(i[0][6:]))
    print(ans)
    return ans


data=["price=80 code=987654 time=2019062113",
      "price=90 code=012345 time=2019062014",
      "price=120 code=987654 time=2019062010",
      "price=110 code=012345 time=2019062009",
      "price=95 code=012345 time=2019062111"]
day="20190620"
code="012345"
solution(code, day, data)