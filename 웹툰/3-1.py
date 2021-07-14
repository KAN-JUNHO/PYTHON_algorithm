from collections import deque
def solution(play_list, listen_time):
    answer = []

    def dfs(idx,cnt,list,time):
        list=deque(list)
        # before
        time -= 1
        while time>0:
            time-=list[idx]
            cnt+=1
            list.rotate(-1)
            if cnt>=len(list):
                break
        answer.append(cnt)
        return cnt

    for i in range(len(play_list)):
        list=play_list[:]
        time=listen_time
        cnt=dfs(i, 1, list,time)
        if dfs(i, 1, list,time) == len(play_list):
            print(cnt)
            break
    else:
        print(max(answer))
solution([101, 100,3, 1, 100],7)