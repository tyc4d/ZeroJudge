while 1:
    try:
        n=int(input())
        num=sorted(list(map(int,input().split())))
        for i in range(0,n):
            print(num[i],end=" ")
    except:
        break
