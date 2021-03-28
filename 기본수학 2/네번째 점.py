    import collections
    x1,y1=list(map(int,input().split()))
    x2,y2=list(map(int,input().split()))
    x3,y3=list(map(int,input().split()))
    x=(collections.Counter([x1,x2,x3]))
    y=(collections.Counter([y1,y2,y3]))

    print(x.most_common(2)[1][0],y.most_common(2)[1][0])
