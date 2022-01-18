while 1:
    try:
        n=int(input())
        d=(n*2-1)-n
        print(d*'_','*',d*'_',sep="")
        for i in range(1,n*2-1,2):
            d=d-i%2
            print(d*'_',(i+2)*'*',d*'_',sep="")
        for i in range(n*2+1,2,-2):
            d=d-i%2
            print(d*'_',(i+2)*'*',d*'_',sep="")
    except:
        break