while 1:
    try:
        num=int(input())%4
        if num==0:
            print('4')
        else:
            print(num)
    except:
        break
