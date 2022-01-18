while 1:
    try:
        n=int(input())
        num=sorted(list(map(int,input().split())))
        for i in range(n):
            print(num[i],end=" ")
        print()
    except:
        break