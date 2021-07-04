def solution(compressed):
    answer = ''

    stack=[]
    for i in compressed:
        if i==")":
            num=""
            alpha=""
            while stack and stack[-1]!="(":
                alpha+=stack[-1]
                stack.pop()
            stack.pop()
            while stack and stack[-1].isdigit():
                num+=stack[-1]
                stack.pop()
            num=num[::-1]
            answer+=alpha*int(num)

            stack.append(answer)
            answer=""

        else:
            stack.append(i)
    ans=[]
    for i in stack:
        ans.append(i[::-1])

    print("".join(ans))
    return "".join(ans)


solution("10(p)")
