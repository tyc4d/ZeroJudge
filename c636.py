while 1:
    try:
        n=(1911+abs(int(input())))%12
        am=['猴','雞','狗','豬','鼠','牛','虎','兔','龍','蛇','馬','羊']
        print(am[n])
    except:
        break