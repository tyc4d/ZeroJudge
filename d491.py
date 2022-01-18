while 1:
    try:
        num=list(map(int,input().split()))
        sum=0
        if num[0]>num[1]:
            c=-1
        else:
            c=1
        for i in range(num[0],num[1]+c,c):
            if i%2==0:
                sum+=i
        print(abs(sum))
    except:
        break