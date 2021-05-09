def solution(t, r):
    answer = []
    for i,g in enumerate(t):
        answer.append([i,g])
    answer.sort(key=lambda x:(x[1],x[0]))
    box=[]
    for i in r:
        for j in range(len(answer)):
            if i == answer[j][1]:
                box.append(answer[j])
        print(box)
        check=[False]*len(box)



    return answer

t=[0,1,3,0]
r=[0,1,2,3]
solution(t,r)