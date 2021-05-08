def solution(n, k, cmd):
    answer = ''
    box=[i for i in range(n)]
    ans=box[:]
    stack=[]
    for order in cmd:
        order=order.split()
        if len(order)>1:
            com=int(order[1])
            if order[0]=="D":
                k+=com
            elif order[0]=="U":
                k-=com
        elif order[0]=="C":
            stack.append(box.pop(k))
            if k>len(box)-1:
                k=len(box)-1
        elif order[0]=="Z":
            if stack[-1]>=k:
                k+=1
            box.insert(stack[-1],stack.pop())
    print(ans)
    print(box)
    while ans:
        if ans[0]==box[0]:
            ans.pop(0)
            box.pop(0)
            answer+="O"
        else:
            ans.pop(0)
            answer+="X"
    return answer

n,k,cmd=8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
solution(n, k, cmd)