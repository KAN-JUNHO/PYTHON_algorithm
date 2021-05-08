def dfs(idx,s):
    ans=[]
    stack = ""
    for i in range(idx,len(s)):
        stack+=s[i]
        if stack in ["zero","one","two","three","four","five","six","seven","eight","nine"]:
            ans.append(stack[:])
            stack=""
        elif s[i].isdigit():
            ans.append(stack[:])
            stack=""
    return ans[:]
def solution(s):
    box=[["0","zero"],
     ["1","one"],
     ["2","two"],
     ["3","three"],
     ["4","four"],
     ["5","five"],
     ["6","six"],
     ["7","seven"],
     ["8","eight"],
     ["9","nine"]]
    answer = []
    a=dfs(0,s)
    i=0
    while i<len(a):
        for j in range(len(box)):
            if box[j][1]==a[i]:
                answer.append(box[j][0])
                break
            elif box[j][0]==a[i]:
                answer.append(box[j][0])
                break
        i+=1
    answer="".join(answer)
    answer=int(answer)
    return answer