while 1:
    try:
        num=list(map(int,input().split()))
        a=num[0]
        b=num[1]
        c=num[2]
        d=0
        if(a&b)==c:
            print("AND")
            d=+1
        if(a|b)==c:
            print("OR")
            d=+1
        if(a!=0)^(b!=0)==c:
            print("XOR")
            d=+1
        if d==0:
            print("IMPOSSIBLE")
    except:
        break