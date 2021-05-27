string = list(input())
visited=[False]*len(string)
ans=[]
def solve(left,right):
    if left==right:
        return
    min_str=min(string[left:right])
    min_idx=string[left:right].index(min_str)+left

    visited[min_idx]=True

    for i in range(len(string)):
        if visited[i]:
            ans.append(string[i])
    print("".join(ans))
    ans.clear()

    solve(min_idx+1,right)
    solve(left,min_idx)


solve(0,len(string))