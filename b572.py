while 1:
    try:
        n=int(input())
        for i in range(n):
            h1,m1,h2,m2,d=list(map(int,input().split()))
            if (h2-h1)*60+(m2-m1)>=d:
                print("Yes")
            elif (h2-h1)*60+(m2-m1)<d:
                print("No")
    except:
        break