n,m=map(int,input().split())

cards = list(map(int,input().split()))
maximum=0
for card1 in range(len(cards)):
    for card2 in range(card1+1,len(cards)):
        for card3 in range(card2+1,len(cards)):
            if cards[card1] +cards[card2] +cards[card3]<=m:
                maximum = max(cards[card1] +cards[card2]+cards[card3],maximum)

print(maximum)