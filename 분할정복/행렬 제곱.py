n,b=map(int,input().split())
box = [list(map(int,input().split())) for i in range(n)]

answer=box[:]

if b==1:
    for i in range(n):
        for j in range(n):
            answer[i][j]=box[i][j]%1000
else:
    for cnt in range(b-1):
        for i in range(n):
            row=[]
            for j in range(n):
                v=0
                for k in range(n):
                    v+=answer[i][k]%1000*box[k][j]%1000
                    v=v%1000
                row.append(v)
            answer.append(row)
        for i in range(n):
            del  answer[0]



for i in answer:
    print(*i)