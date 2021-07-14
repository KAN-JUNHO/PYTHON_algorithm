from collections import deque
def solution(play_list, listen_time):
    answer = 0
    idx= play_list.index(max(play_list))+1
    if idx == len(play_list):
        idx=0
    cnt=1

    play_list=deque(play_list)
    # before
    listen_time -= 1
    while listen_time>0:
        listen_time-=play_list[idx]
        cnt+=1
        play_list.rotate(-1)
        if cnt>=len(play_list):
            break
    print(cnt)
    return cnt

solution([101, 100,3, 1, 100],7)