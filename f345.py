while 1:
    try:
        n=int(input())
        num=list(map(int,input().split()))[::-1]
        for i in range(n):
            print(num[i],end=" ")
        print()
    except:
        break