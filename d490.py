while 1:
    try:
        num=list(map(int,input().split()))
        sum=0
        for i in range(num[0],num[1]+1):
            if i%2==0:
                sum+=i
        print(sum)
    except:
        break