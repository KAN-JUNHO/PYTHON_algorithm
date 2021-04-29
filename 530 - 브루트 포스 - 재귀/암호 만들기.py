l,c = map(int,input().split())
alpha=list(map(str,input().split()))
alpha.sort()
box=[]
vowel=["a","e","i","o","u"]
def dfs(pos):
    if len(box)==l:
        cnt=0
        for i in box:
            if i in vowel:
                cnt+=1
        if cnt>0 and 1<l-cnt:
            print("".join(box))
        return
    for i in range(pos,c):
        box.append(alpha[i])
        dfs(i+1)
        box.pop()

dfs(0)