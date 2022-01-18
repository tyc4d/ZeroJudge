while 1:
    try:
        num=int(input())
        best=0
        a=(num//1000)*100
        b=(num//2000)*200
        if a>b:
            best=1
            ans=num-a
        else:
            best=0
            ans=num-b
        print(ans,best)
    except:
        break
