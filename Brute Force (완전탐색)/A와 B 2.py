s=input()
t=input()

def dfs(t):
    if len(s)==len(t):
        if s==t:
            print(1)
            exit(0)
        return
    if t[0]=="B":
        t=t[::-1]
        t=t[:-1]
        dfs(t)
        t+="B"
        t=t[::-1]
    if t[-1]=="A":
        t=t[:-1]
        dfs(t)
        t+="A"
dfs(t)
print(0)

