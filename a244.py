while 1:
    try:
        n=int(input())
        for i in range(n):
            m=list(map(int, input().split()))
            if m[0]==1:
                print(m[1]+m[2])
            elif m[0]==2:
                print(m[1]-m[2])
            elif m[0]==3:
                print(m[1]*m[2])
            elif m[0]==4:
                print(m[1]//m[2])
    except:
        break