import itertools

box=list(map(str,input()))
idx=[]
stack=[]
ans=[]
for i,j in enumerate(box):
    if j=="(":
        box[i]=""
        stack.extend([i])
    elif j==")":
        box[i]=""
        idx.append([stack.pop(),i])
for i in range(len(idx)):
    for j in itertools.combinations(idx,i):
        answer=box[:]
        for v,w in j:
            answer[v]="("
            answer[w]=")"
        ans.append("".join(answer))
ans=list(set(ans))
for i in sorted(ans):
    print(i)