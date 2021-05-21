cash=int(input())
stock=list(map(int,input().split()))
jun=sung=cash
jun_stock=0
sung_stock=0
up=0
down=0
for i in range(len(stock)):
    if jun>=stock[i]:
        jun_stock+=jun//stock[i]
        jun=jun%stock[i]

    if i>0 and stock[i]>stock[i-1]:
        down=0
        up+=1
        if up==3:
            sung+=sung_stock*stock[i]
            sung_stock=0
            up=0
    elif i>0 and stock[i-1]>stock[i] and sung>=stock[i]:
        up=0
        down+=1
        if down>=3:
            sung_stock+=sung//stock[i]
            sung=sung%stock[i]

jun_money = jun_stock*stock[-1] + jun
sung_money = sung_stock*stock[-1] + sung

if jun_money>sung_money:
    print("BNP")
elif jun_money<sung_money:
    print("TIMING")
else:
    print("SAMESAME")