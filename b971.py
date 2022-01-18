while 1:
    try:
        num=input().split()
        a1=int(num[0])
        an=int(num[1])
        d=int(num[2])
        for i in range(a1-1,an//2+1):
            print(a1+d*i,end=" ")
    except:
        break