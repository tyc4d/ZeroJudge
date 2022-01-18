while 1:
    try:
        n=int(input())
        d=(n*2-1)-n
        m=d*'_'+'+'+d*'_'
        print(m[:n])
        for i in range(1,n*2-1,2):
            d=d-i%2
            tmp=d*'_'+(i+2)*'+'+d*'_'
            print(tmp[:n])
    except:
        break