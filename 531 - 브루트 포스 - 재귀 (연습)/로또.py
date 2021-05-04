import collections
import itertools
while True:
    lotto = collections.deque(map(int,input().split()))
    if not lotto[0]:
        break
    lotto.popleft()
    a=list(itertools.combinations(lotto,6))
    for i in a:
        print(*i)
    print()