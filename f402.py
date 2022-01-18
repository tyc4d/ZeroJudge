while 1:
    try:
        n=int(input())
        num=sorted(list(map(int,input().split())))
        vnum=[]
        for i in range(len(num)):
            if num[i]<=25:
                vnum.append(num[i])
        if len(vnum)>=5:
            print("5")
        elif len(vnum)<5:
            print(len(vnum))
    except:
        break