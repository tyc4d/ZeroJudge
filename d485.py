while 1:
    try:
        num=list(map(int, input().split()))
        count=0
        for i in range(num[0],num[-1]+1):
            if i%2==0:
                count=count+1
        print(count)
        print()
    except:
        break